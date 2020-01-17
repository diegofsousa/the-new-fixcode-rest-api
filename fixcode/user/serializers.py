from rest_framework import serializers
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'email', 'url']

class SimpleUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'email']

class UserSerializerForRegister(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ["username","name","email","password"]