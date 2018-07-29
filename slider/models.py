from django.db import models


class Slide(models.Model):
	title = models.CharField(max_length=50, default='', blank=True, verbose_name='عنوان')
	description = models.CharField(max_length=100, default='', blank=True, verbose_name='توضیحات')
	image = models.ImageField(upload_to='images/slider', verbose_name='تصویر')
	url = models.URLField(verbose_name='لینک')
	order = models.PositiveIntegerField(default=0, verbose_name='شماره',
		help_text=
		'اسلایدها بر اساس این شماره مرتب می شوند (کوچک ترین به بزرگترین)')
	active = models.BooleanField(default=False, verbose_name='فعال',
		help_text='اسلاید فعال در ابتدا نمایش داده می شود')

	def __str__(self):
		if self.title:
			return self.title
		elif self.url:
			return self.url

	class Meta:
		ordering = ('order',)
