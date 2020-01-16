from django.shortcuts import render
from .serializers import FirstAccessSerializer, SecondAccessSerializer
from rest_framework import generics
from fixcode.commons.email import first_register_email
#from fixcode.user.models
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TemporalyDataUser
from fixcode.commons.utils import is_valid_and_return_uuid
from rest_framework.serializers import ValidationError as RestFieldValidationError
from rest_framework.exceptions import NotFound

from rest_framework import status



class FirstAccessView(generics.CreateAPIView):
	serializer_class = FirstAccessSerializer

	def perform_create(self, serializer):
		post_save_object = serializer.save()
		name, email, link = post_save_object.first_name, post_save_object.email, post_save_object.hash_for_link_activation
		first_register_email(name, email, link)
		print(name, email, link)

class SecondAccessView(generics.GenericAPIView):
	serializer_class = SecondAccessSerializer

	def get(self, request, *args, **kwargs):
		link = request.GET.get("link", "")
		filter_temp_user_by_token = TemporalyDataUser. \
			objects. \
			filter(hash_for_link_activation=is_valid_and_return_uuid(link))
		if filter_temp_user_by_token.count() != 0:
			serializer_temp_user = FirstAccessSerializer(filter_temp_user_by_token.first())
			return Response(serializer_temp_user.data)
		raise NotFound(detail="Token expirado ou inexistente", code=404)
