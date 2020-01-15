from django.core.mail import EmailMessage
from django.conf import settings

# TODO: Refatore this

def first_register_email(name, email, link):
	email = EmailMessage(
	    '[FixCode] - Podemos ativar sua conta agora?',
	    'Olá {}, tudo bem? Para ativr a sua conta precisamos que você defina uma senha no link a seguir: {}'.format(name, link),
	    settings.EMAIL_HOST_USER,
	    [email,],
	    [],
	    headers={'Message-ID': 'FixCode'},
	)
	email.send(fail_silently=False)