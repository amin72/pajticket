from django.db import models



class News(models.Model):
	title = models.CharField(max_length=255, verbose_name='عنوان')
	text = models.TextField(verbose_name='متن')
	date = models.DateTimeField(auto_now_add=True, verbose_name='زمان')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'News'
