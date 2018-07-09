from django.db import models


class Ticket(models.Model):
	pass



class People(models.Model):
	GENDERS = (
		('f', 'Female'),
		('m', 'Male')
	)
	
	first_name = models.CharField(max_length=255, verbose_name='نام')
	last_name = models.CharField(max_length=255, verbose_name='نام خانوادگی')
	birth_day = models.DateTimeField(verbose_name='تاریخ تولد', blank=True)
	gender = models.CharField(max_length=255, verbose_name='جنسیت',
		choices=GENDERS)

	def __str__(self):
		return self.first_name + ' ' + self.last_name



class Actor(models.Model):
	person = models.ForeignKey(People, on_delete=models.CASCADE,
		verbose_name='کاربر')



class Director(models.Model):
	person = models.ForeignKey(People, on_delete=models.CASCADE,
		verbose_name='کاربر')



class Writer(models.Model):
	person = models.ForeignKey(People, on_delete=models.CASCADE,
		verbose_name='کاربر')




class Language(models.Model):
	pass



class Genre(models.Model):
	title = models.CharField(max_length=30, verbose_name='ژانر')



class Country(models.Model):
	name = models.CharField(max_length=40, verbose_name='نام')



class Film(models.Model):
	title = models.CharField(max_length=255, verbose_name='عنوان')
	director = models.ForeignKey(Director, verbose_name='کارگردان')
	runnig_time = models.DateTimeField(auto_now_add=True,
		verbose_name='زمان نمایش فیلم')
	release_time = models.DateTimeField(auto_now_add=True, verbose_name='')

	length = models.PositiveIntegerField(verbose_name='مدت زمان')
	language = models.ForeignKey(Language, verbose_name='زبان',
		on_delete=models.CASCADE)
	country = models.ForeignKey(Country, verbose_name='محصول',
		on_delete=models.CASCADE)
	actors = models.ManyToManyField(Actor, verbose_name='ستارگان')
	description = models.TextField(verbose_name='خلاصه داستان')
	genre = models.ForeignKey(Genre, verbose_name='ژانر')
	writer = models.ForeignKey(Writer, verbose_name='نویسنده')
