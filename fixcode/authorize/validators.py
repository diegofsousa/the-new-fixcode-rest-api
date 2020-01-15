from django.core.exceptions import ValidationError
from rest_framework.serializers import ValidationError as RestFieldValidationError

def _regex_validator(regex, val):
	import re
	if re.search(regex, val) != None:
		raise RestFieldValidationError('Este campo aceita apenas valores no formato {}'.format(regex))