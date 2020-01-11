from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .models import User

class UserAdminCreationForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['username', 'name', 'email', 'is_staff']


class UserAdminForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username', 'email', 'name', 'is_active', 'is_staff']

class PasswordResetForm(PasswordResetForm):
	def clean_email(self):
		amount = get_user_model()._default_manager.filter(
			email__iexact=self.cleaned_data.get('email'), is_active=True).count()
		if(amount < 1):
			raise forms.ValidationError('Lamentamos, mas não reconhecemos esse endereço de e-mail.')
		return self.cleaned_data.get('email')