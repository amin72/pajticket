from django.db import models

from tinymce.models import HTMLField


class Advertisement(models.Model):
	text = HTMLField(blank=True, default='', verbose_name='متن')
	url = models.URLField(verbose_name='لینک')
	image = models.ImageField(upload_to='images/advertisements',
		verbose_name='تصویر')
	order = models.PositiveIntegerField(default=0, verbose_name='شماره',
		help_text=
		'تبلیغات بر اساس این شماره مرتب می شوند (کوچک ترین به بزرگترین)')

	def __str__(self):
		if self.text:
			return self.text
		else:
			return self.url

	class Meta:
		ordering = ('order',)
