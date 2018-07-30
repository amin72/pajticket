from django.db import models

from tinymce.models import HTMLField


class News(models.Model):
	title = models.CharField(max_length=255, verbose_name='عنوان')
	text = HTMLField(verbose_name='متن')
	date = models.DateTimeField(auto_now_add=True, verbose_name='زمان')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'News'
