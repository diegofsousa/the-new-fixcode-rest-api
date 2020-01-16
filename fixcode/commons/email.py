from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# TODO: Refatore this

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