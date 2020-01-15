from django.db import models
from mongoengine import Document, EmbeddedDocument, fields
from datetime import datetime
from uuid import uuid4

class TemporalyDataUser(Document):
	first_name = fields.StringField(required=True)
	last_name = fields.StringField(required=True)
	username = fields.StringField(required=True)
	email = fields.EmailField(required=True)
	created_at = fields.DateTimeField(default=datetime.now)
	hash_for_link_activation = fields.UUIDField(default=uuid4)