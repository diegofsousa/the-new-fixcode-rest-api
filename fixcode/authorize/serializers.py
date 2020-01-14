from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import TemporalyDataUser

class FirstAccessSerializer(DocumentSerializer):
    class Meta:
        model = TemporalyDataUser
        fields = ["username","first_name","last_name","email", "password"]