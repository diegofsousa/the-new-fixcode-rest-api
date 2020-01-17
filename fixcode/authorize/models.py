from django.db import models
from mongoengine import Document, EmbeddedDocument, fields
from datetime import datetime
from uuid import uuid4

class TemporalyDataUser(Document):
	name = fields.StringField(required=True)
	username = fields.StringField(required=True)
	email = fields.EmailField(required=True)
	created_at = fields.DateTimeField(default=datetime.now)
	hash_for_link_activation = fields.UUIDField(default=uuid4)

	class Meta:
		verbose_name = 'TempUser'
		verbose_name_plural = 'TempUsers'

	def first_name(self):
		return self.name.split(" ")[0]

	def __str__(self):
		return self.name