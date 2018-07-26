from django import forms
from django.contrib.auth.forms import (UserCreationForm,
	AuthenticationForm, UserChangeForm)
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit


class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.layout = Layout(
			'username',
			'password',
			ButtonHolder(
				Submit('login', 'ورود', css_class='btn-primary')
			)
		)


def validate_email_unique(value):
	exists = User.objects.filter(email=value)
	if exists:
		raise ValidationError(
			'ایمیل {} قبلا استفاده شده است'.format(value)
		)


class RegistrationForm(UserCreationForm):
	first_name = forms.CharField(max_length=255, label='نام')
	last_name = forms.CharField(max_length=255, label='نام خانوادگی')
	email = forms.EmailField(max_length=255, label='ایمیل',
		validators=[validate_email_unique])

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.layout = Layout(
			'first_name',
			'last_name',
			'email',
			'username',
			'password1',
			'password2',
			ButtonHolder(
				Submit('register', 'عضویت', css_class='btn-primary')
			)
		)

	def save(self):
		user = super().save(self)
		user.first_name = self.cleaned_data.get('first_name')
		user.last_name = self.cleaned_data.get('last_name')
		user.email = self.cleaned_data.get('email')
		user.save()
		return user


class UserEditForm(forms.ModelForm):
	first_name = forms.CharField(max_length=255, label='نام')
	last_name = forms.CharField(max_length=255, label='نام خانوادگی')
	email = forms.EmailField(max_length=255, label='ایمیل')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.layout = Layout(
			'first_name', 'last_name', 'email',
			ButtonHolder(
				Submit('update', 'ویرایش', css_class='btn-primary')
			)
		)

	def clean_email(self):
		username = self.instance.username
		email = self.cleaned_data.get('email')
		users = User.objects.filter(email__iexact=email).exclude(username__iexact=username)
		if users:
			raise ValidationError('ایمیل {} قبلا استفاده شده است'.format(email))
		return email.lower()

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')
