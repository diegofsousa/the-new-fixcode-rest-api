from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError as RestFieldValidationError
from rest_framework.exceptions import NotFound
from rest_framework import status
from fixcode.commons.email import first_register_email, end_register_email
from fixcode.commons.utils import is_valid_and_return_uuid
from fixcode.user.models import User
from fixcode.user.serializers import UserSerializerForRegister, SimpleUserSerializer
from fixcode.user.service import temp_user_to_persist_user
from .models import TemporalyDataUser
from .serializers import FirstAccessSerializer, SecondAccessSerializer

class FirstAccessView(generics.CreateAPIView):
	serializer_class = FirstAccessSerializer

	def perform_create(self, serializer):
		post_save_object = serializer.save()
		name, email, link = post_save_object.first_name(), post_save_object.email, post_save_object.hash_for_link_activation
		first_register_email(name, email, link)
		print(name, email, link)

class SecondAccessView(generics.GenericAPIView):
	serializer_class = SecondAccessSerializer

	def _query_link_is_valid(self, link):
		return TemporalyDataUser. \
				objects. \
				filter(hash_for_link_activation=is_valid_and_return_uuid(link))

	def get(self, request, *args, **kwargs):
		link = request.GET.get("link", "")
		filter_temp_user_by_token = self._query_link_is_valid(link)
		if filter_temp_user_by_token.count() != 0:
			serializer_temp_user = FirstAccessSerializer(filter_temp_user_by_token.first())
			return Response(serializer_temp_user.data)
		raise NotFound(detail="Token expirado ou inexistente", code=404)

	def post(self, request, *args, **kwargs):
		link = request.GET.get("link", "")
		filter_temp_user_by_token = self._query_link_is_valid(link)
		if filter_temp_user_by_token.count() == 0:
			raise NotFound(detail="Token expirado ou inexistente", code=404)

		serializer_persist_pass = SecondAccessSerializer(data=request.data)

		if serializer_persist_pass.is_valid() == False:
			return Response(serializer_persist_pass.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
			mongo_pass_to_postgres = temp_user_to_persist_user(filter_temp_user_by_token.first(),
															   serializer_persist_pass.data["password"])
			serializer_data_user_persist = SimpleUserSerializer(mongo_pass_to_postgres)
			end_register_email(mongo_pass_to_postgres.name,
								mongo_pass_to_postgres.email)
			return Response(serializer_data_user_persist.data)
