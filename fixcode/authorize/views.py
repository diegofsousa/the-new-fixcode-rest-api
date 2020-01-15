from django.shortcuts import render
from .serializers import FirstAccessSerializer
from rest_framework import generics
from fixcode.commons.email import first_register_email


class FirstAccessView(generics.CreateAPIView):
	serializer_class = FirstAccessSerializer

	def perform_create(self, serializer):
		post_save_object = serializer.save()
		name, email, link = post_save_object.first_name, post_save_object.email, post_save_object.hash_for_link_activation
		# first_register_email(name, email, link)
		print(name, email, link)