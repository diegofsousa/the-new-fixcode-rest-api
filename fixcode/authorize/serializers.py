from rest_framework import serializers
from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import TemporalyDataUser
from .validators import _regex_validator


class FirstAccessSerializer(DocumentSerializer):
	class Meta:
		model = TemporalyDataUser
		fields = ["username","first_name","last_name","email"]

	def validate_username(self, value):
		_regex_validator('[^0-9a-zA-Z]', value)
		return value