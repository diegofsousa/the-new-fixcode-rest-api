from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from celery import shared_task

@shared_task
def first_register_email(name, email, link):

	context = {
		"name":name,
		"link":link
	}

	EMAIL_TEMPLATE = render_to_string('accounts/email_verification.html', context)
	SUBJECT = "Podemos ativar sua conta agora?"

	email = EmailMessage(SUBJECT, EMAIL_TEMPLATE, settings.EMAIL_HOST_USER, [email,])
	email.content_subtype = "html" 
	email.send(fail_silently=False)

@shared_task
def end_register_email(name, email):

	context = {
		"name":name,
	}

	EMAIL_TEMPLATE = render_to_string('accounts/end_verification.html', context)
	SUBJECT = "Conta ativada com sucesso!"

	email = EmailMessage(SUBJECT, EMAIL_TEMPLATE, settings.EMAIL_HOST_USER, [email,])
	email.content_subtype = "html" 
	email.send(fail_silently=False)