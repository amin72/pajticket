from django.db import models
from django.contrib.auth.models import User


class Place(models.Model):
	name = models.CharField(max_length=255, verbose_name='مکان')

	def __str__(self):
		return self.name


class Ticket(models.Model):
	ROWS = (
		(1, 'اول'),
		(2, 'دوم'),
		(3, 'سوم'),
	)

	user = models.ForeignKey(User, verbose_name='مشتری',
		on_delete=models.CASCADE)
	title = models.CharField(max_length=255, verbose_name='عنوان')
	price = models.FloatField(verbose_name='مبلغ')
	row = models.PositiveIntegerField(choices=ROWS, verbose_name='ردیف')
	place = models.ForeignKey(Place, on_delete=models.CASCADE,
		verbose_name='مکان')

	def __str__(self):
		return '{}, {}'.format(self.title, self.place)

	def save(self):
		# add 20% to ticket price if row is 1
		if self.row == 1:
			self.price += (self.price / 100) * 20

		# add 10% to ticket price if row is 2
		elif self.row == 2:
			self.price += (self.price / 100) * 10
		# row 3 is already set
		return super().save()

	class Meta:
		abstract = True


class People(models.Model):
	GENDERS = (
		('f', 'Female'),
		('m', 'Male')
	)
	
	first_name = models.CharField(max_length=255, verbose_name='نام')
	last_name = models.CharField(max_length=255, verbose_name='نام خانوادگی')
	birth_day = models.DateTimeField(verbose_name='تاریخ تولد', blank=True,
		default='')
	gender = models.CharField(max_length=255, verbose_name='جنسیت',
		choices=GENDERS)

	def __str__(self):
		return self.first_name + ' ' + self.last_name

	class Meta:
		verbose_name_plural = 'People'


class Actor(models.Model):
	person = models.ForeignKey(People, on_delete=models.CASCADE,
		verbose_name='کاربر')

	def __str__(self):
		return str(self.person)


class Director(models.Model):
	person = models.ForeignKey(People, on_delete=models.CASCADE,
		verbose_name='کاربر')

	def __str__(self):
		return str(self.person)


class Writer(models.Model):
	person = models.ForeignKey(People, on_delete=models.CASCADE,
		verbose_name='کاربر')

	def __str__(self):
		return str(self.person)


class Producer(models.Model):
	person = models.ForeignKey(People, on_delete=models.CASCADE,
		verbose_name='کاربر')

	def __str__(self):
		return str(self.person)


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

	class Meta:
		verbose_name_plural = 'Countries'


class Film(models.Model):
	title = models.CharField(max_length=255, verbose_name='عنوان')
	director = models.ForeignKey(Director, verbose_name='کارگردان')
	producer = models.ForeignKey(Producer, verbose_name='تهیه کننده')
	release_date = models.DateTimeField(auto_now_add=True,
		verbose_name='زمان انتشار')
	running_time = models.DateTimeField(verbose_name='زمان اکران فیلم')
	length = models.PositiveIntegerField(verbose_name='مدت زمان')
	language = models.ForeignKey(Language, verbose_name='زبان',
		on_delete=models.CASCADE)
	country = models.ForeignKey(Country, verbose_name='محصول',
		on_delete=models.CASCADE)
	actors = models.ManyToManyField(Actor, verbose_name='ستارگان')
	description = models.TextField(verbose_name='خلاصه داستان')
	genre = models.ForeignKey(Genre, verbose_name='ژانر')
	writer = models.ForeignKey(Writer, verbose_name='نویسنده')
	cover = models.ImageField(upload_to='images/films/', verbose_name='کاور', default='')

	def __str__(self):
		return self.title


class FilmTicket(Ticket):
	film = models.ForeignKey(Film, on_delete=models.CASCADE,
		verbose_name='فیلم')
	price = models.FloatField(verbose_name='مبلغ')

	class Meta:
		verbose_name_plural = 'Film Tickets'


class Theater(models.Model):
	title = models.CharField(max_length=255, verbose_name='عنوان')
	director = models.ForeignKey(Director, verbose_name='کارگردان')
	running_time = models.DateTimeField(verbose_name='زمان نمایش فیلم')
	actors = models.ManyToManyField(Actor, verbose_name='ستارگان')
	description = models.TextField(verbose_name='خلاصه داستان')
	genre = models.ForeignKey(Genre, verbose_name='ژانر')
	writer = models.ForeignKey(Writer, verbose_name='نویسنده')
	cover = models.ImageField(upload_to='images/theaters/',
		verbose_name='کاور', default='')

	def __str__(self):
		return self.title


class TheaterTicket(Ticket):
	theater = models.ForeignKey(Theater, on_delete=models.CASCADE,
		verbose_name='تئاتر')

	class Meta:
		verbose_name_plural = 'Theater Tickets'


class Song(models.Model):
	title = models.CharField(max_length=255, verbose_name='عنوان')
	singer = models.ForeignKey(People, verbose_name='خواننده')
	length = models.PositiveIntegerField(verbose_name='مدت زمان')
	cover = models.ImageField(upload_to='images/songs/', verbose_name='کاور', default='')

	def __str__(self):
		return self.title + ", " + str(self.singer)


class Concert(models.Model):
	title = models.CharField(max_length=255, verbose_name='عنوان')
	artist = models.ForeignKey(People, on_delete=models.CASCADE,
		verbose_name='خواننده')
	songs = models.ManyToManyField(Song, verbose_name='ترانه ها')
	running_time = models.DateTimeField(verbose_name='زمان کنسرت')
	length = models.PositiveIntegerField(verbose_name='مدت اجرا کنسرت')
	description = models.TextField(verbose_name='توضیحات')
	place = models.ForeignKey(Place, verbose_name='مکان')

	def __str__(self):
		return self.title


class ConcertTicket(Ticket):
	concert = models.ForeignKey(Concert, on_delete=models.CASCADE,
		verbose_name='کنسرت')

	class Meta:
		verbose_name_plural = 'Concert Tickets'
