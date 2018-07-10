from django.db import models


class Ticket(models.Model):
	title = models.CharField(max_length=255, verbose_name='عنوان')
	place = models.CharField(max_length=255, verbose_name='مکان')
	date = models.DateTimeField(verbose_name='زمان')

	def __str__(self):
		return '{}, at {}, on {}'.format(self.title, self.place, self.date)



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
	name = models.CharField(max_length=30, verbose_name='زبان')

	def __str__(self):
		return self.name



class Genre(models.Model):
	title = models.CharField(max_length=30, verbose_name='ژانر')

	def __str__(self):
		return self.title



class Country(models.Model):
	name = models.CharField(max_length=40, verbose_name='نام')

	def __str__(self):
		return self.name



class Film(models.Model):
	title = models.CharField(max_length=255, verbose_name='عنوان')
	director = models.ForeignKey(Director, verbose_name='کارگردان')
	release_time = models.DateTimeField(auto_now_add=True,
		verbose_name='زمان انتشار')
	runnig_time = models.DateTimeField(auto_now_add=True,
		verbose_name='زمان اجرا فیلم')
	length = models.PositiveIntegerField(verbose_name='مدت زمان')
	language = models.ForeignKey(Language, verbose_name='زبان',
		on_delete=models.CASCADE)
	country = models.ForeignKey(Country, verbose_name='محصول',
		on_delete=models.CASCADE)
	actors = models.ManyToManyField(Actor, verbose_name='ستارگان')
	description = models.TextField(verbose_name='خلاصه داستان')
	genre = models.ForeignKey(Genre, verbose_name='ژانر')
	writer = models.ForeignKey(Writer, verbose_name='نویسنده')

	def __str__(self):
		return self.title



class FilmTicket(Ticket):
	film = models.ForeignKey(Film, on_delete=models.CASCADE,
		verbose_name='فیلم')

	def __str__(self):
		return self.concert + ', ' + self.ticket



class Theater(models.Model):
	title = models.CharField(max_length=255, verbose_name='عنوان')
	director = models.ForeignKey(Director, verbose_name='کارگردان')
	runnig_time = models.DateTimeField(auto_now_add=True,
		verbose_name='زمان نمایش فیلم')
	actors = models.ManyToManyField(Actor, verbose_name='ستارگان')
	description = models.TextField(verbose_name='خلاصه داستان')
	genre = models.ForeignKey(Genre, verbose_name='ژانر')
	writer = models.ForeignKey(Writer, verbose_name='نویسنده')

	def __str__(self):
		return self.title



class TheaterTicket(Ticket):
	theater = models.ForeignKey(Theater, on_delete=models.CASCADE,
		verbose_name='تئاتر')

	def __str__(self):
		return self.concert + ', ' + self.ticket



class Song(models.Model):
	title = models.CharField(max_length=255, verbose_name='عنوان')
	singer = models.ForeignKey(People, verbose_name='خواننده')
	length = models.PositiveIntegerField(verbose_name='مدت زمان')

	def __str__(self):
		return self.title + ", " + self.singer



class Concert(models.Model):
	title = models.CharField(max_length=255, verbose_name='عنوان')
	song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name='خواننده')
	date = models.DateTimeField(auto_now_add=True, verbose_name='زمان کنسرت')
	description = models.TextField(verbose_name='خلاصه داستان')

	def __str__(self):
		return self.title



class ConcertTicket(Ticket):
	concert = models.ForeignKey(Concert, on_delete=models.CASCADE,
		verbose_name='کنسرت')

	def __str__(self):
		return self.concert + ', ' + self.ticket
