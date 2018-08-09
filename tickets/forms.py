from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Layout, Submit

from . import models


class FilmTicket(forms.ModelForm):
	class Meta:
		model = models.FilmTicket
		fields = ('row', 'place')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			'row',
			'place',
			ButtonHolder(
				Submit('buy', 'خرید', css_class='btn-primary'),
			)
		)


class TheaterTicket(forms.ModelForm):
	class Meta:
		model = models.TheaterTicket
		fields = ('row', 'place')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			'row',
			'place',
			ButtonHolder(
				Submit('but', 'خرید', css_class='btn-primary')
			)
		)


class ConcertTicket(forms.ModelForm):
	class Meta:
		model = models.ConcertTicket
		fields = ('row',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			'row',
			ButtonHolder(
				Submit('buy', 'خرید', css_class='btn-primary')
			)
		)


class ContactUsForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			'email',
			'phone_number',
			'bio',
			'text',
			ButtonHolder(
				Submit('submit', 'ارسال', css_class='btn-primary')
			)
		)

	class Meta:
		model = models.ContactUs
		fields = ('email', 'phone_number', 'bio', 'text')
