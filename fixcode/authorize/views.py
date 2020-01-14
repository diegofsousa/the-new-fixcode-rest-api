from django.shortcuts import render
from .serializers import FirstAccessSerializer
from rest_framework import generics


class FirstAccessView(generics.CreateAPIView):
    serializer_class = FirstAccessSerializer