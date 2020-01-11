from django.db import models
from django.core import validators
from django.contrib.auth.models import (
	AbstractBaseUser, UserManager, PermissionsMixin
)
from easy_thumbnails.fields import ThumbnailerImageField
import re

class User(AbstractBaseUser, PermissionsMixin):

	username = models.CharField(
		'Username', max_length=30, unique=True, validators=[
			validators.RegexValidator(
				re.compile('^[\w.@+-]+$'),
				'Enter a valid username. '
				'This value must contain only letters, numbers, and '
				'the characters: @/./+/-/_ .'
				, 'invalid'
			)
		],
		help_text='A short name that will be used to uniquely \
		identify you on the platform.'
	)
	name = models.CharField('Name', max_length=100, blank=True)
	email = models.EmailField('E-mail', unique=True)
	is_staff = models.BooleanField('Staff', default=False)
	is_active = models.BooleanField('Active', default=True)
	date_joined = models.DateTimeField('Date Joined', auto_now_add=True)	
	avatar = ThumbnailerImageField(
		upload_to="avatar",
		blank=True,
		resize_source=dict(size=(215, 215), crop=True)
	)

	bio = models.CharField('Bio', max_length=100, blank=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	objects = UserManager()

	class Meta:
		verbose_name = 'User'
		verbose_name_plural = 'Users'