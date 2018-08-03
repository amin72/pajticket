from django.db import models

from tinymce.models import HTMLField
from django_jalali.db import models as jmodels


class News(models.Model):
	title = models.CharField(max_length=255, verbose_name='عنوان')
	text = HTMLField(verbose_name='متن')
	date = jmodels.jDateTimeField(auto_now_add=True, verbose_name='زمان')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'News'
