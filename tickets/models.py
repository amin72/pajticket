from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import RegexValidator
from django.utils import timezone

from tinymce.models import HTMLField
from django_jalali.db import models as jmodels

from .helpers import calculate_price_by_row


class Place(models.Model):
	name = models.CharField(max_length=255, verbose_name='نام')
	address = models.CharField(max_length=255, verbose_name='آدرس')

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
	chair_number = models.PositiveIntegerField(verbose_name='شماره صندلی')
	place = models.ForeignKey(Place, on_delete=models.CASCADE,
		verbose_name='مکان')

	def __str__(self):
		return '{}, {}'.format(self.title, self.place)

	def save(self):
		self.price = calculate_price_by_row(self.price, self.row)
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
	birth_day = jmodels.jDateTimeField(verbose_name='تاریخ تولد', blank=True,
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
	director = models.ForeignKey(Director, verbose_name='کارگردان',
		on_delete=models.CASCADE)
	producer = models.ForeignKey(Producer, verbose_name='تهیه کننده',
		on_delete=models.CASCADE)
	release_date = jmodels.jDateField(verbose_name='سال ساخت')
	running_time = jmodels.jDateTimeField(verbose_name='زمان اکران')
	length = models.PositiveIntegerField(verbose_name='مدت زمان')
	language = models.ForeignKey(Language, verbose_name='زبان',
		on_delete=models.CASCADE)
	country = models.ForeignKey(Country, verbose_name='محصول',
		on_delete=models.CASCADE)
	actors = models.ManyToManyField(Actor, verbose_name='ستارگان')
	description = HTMLField(verbose_name='خلاصه داستان')
	genre = models.ForeignKey(Genre, verbose_name='ژانر',
		on_delete=models.CASCADE)
	writer = models.ForeignKey(Writer, verbose_name='نویسنده',
		on_delete=models.CASCADE)
	cover = models.ImageField(upload_to='images/films/', verbose_name='کاور', default='')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('tickets:film_detail', kwargs={'pk': self.pk})

	class Meta:
		ordering = ('-id',)


class FilmTicket(Ticket):
	film = models.ForeignKey(Film, on_delete=models.CASCADE,
		verbose_name='فیلم')
	price = models.FloatField(verbose_name='مبلغ')

	class Meta:
		verbose_name_plural = 'Film Tickets'


class Theater(models.Model):
	title = models.CharField(max_length=255, verbose_name='عنوان')
	director = models.ForeignKey(Director, verbose_name='کارگردان',
		on_delete=models.CASCADE)
	producer = models.ForeignKey(Producer, verbose_name='تهیه کننده',
		on_delete=models.CASCADE)
	running_time = jmodels.jDateTimeField(verbose_name='زمان نمایش فیلم')
	length = models.PositiveIntegerField(verbose_name='مدت زمان')
	language = models.ForeignKey(Language, verbose_name='زبان',
		on_delete=models.CASCADE)
	actors = models.ManyToManyField(Actor, verbose_name='ستارگان')
	description = HTMLField(verbose_name='خلاصه داستان')
	genre = models.ForeignKey(Genre, verbose_name='ژانر',
		on_delete=models.CASCADE)
	writer = models.ForeignKey(Writer, verbose_name='نویسنده',
		on_delete=models.CASCADE)
	cover = models.ImageField(upload_to='images/theaters/',
		verbose_name='کاور', default='')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('tickets:theater_detail', kwargs={'pk': self.pk})

	class Meta:
		ordering = ('-id',)


class TheaterTicket(Ticket):
	theater = models.ForeignKey(Theater, on_delete=models.CASCADE,
		verbose_name='تئاتر')

	class Meta:
		verbose_name_plural = 'Theater Tickets'


class Song(models.Model):
	title = models.CharField(max_length=255, verbose_name='عنوان')
	singer = models.ForeignKey(People, verbose_name='خواننده',
		on_delete=models.CASCADE)
	length = models.PositiveIntegerField(verbose_name='مدت زمان')

	def __str__(self):
		return self.title + ", " + str(self.singer)


class Concert(models.Model):
	title = models.CharField(max_length=255, verbose_name='عنوان')
	artist = models.ForeignKey(People, on_delete=models.CASCADE,
		verbose_name='خواننده')
	songs = models.ManyToManyField(Song, verbose_name='ترانه ها')
	running_time = jmodels.jDateTimeField(verbose_name='زمان کنسرت')
	length = models.PositiveIntegerField(verbose_name='مدت اجرا کنسرت')
	description = HTMLField(verbose_name='توضیحات')
	place = models.ForeignKey(Place, verbose_name='مکان',
		on_delete=models.CASCADE)
	cover = models.ImageField(upload_to='images/concerts/',
		verbose_name='کاور')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('tickets:concert_detail', kwargs={'pk': self.pk})

	class Meta:
		ordering = ('-id',)


class ConcertTicket(Ticket):
	concert = models.ForeignKey(Concert, on_delete=models.CASCADE,
		verbose_name='کنسرت')

	class Meta:
		verbose_name_plural = 'Concert Tickets'


class ContactUs(models.Model):
	name = models.CharField(max_length=255, verbose_name='نام و نام خانوادگی')
	email = models.EmailField(verbose_name='ایمیل')

	phone_regex = RegexValidator(regex=r'^09\d{9}$',
    	message="شماره تماس باید به این فرمت وارد شود: 09123456789")
	phone_number = models.CharField(validators=[phone_regex], max_length=11,
    	blank=True, verbose_name='شماره تماس') # validators should be a list

	text = models.TextField(verbose_name='متن')
	date = jmodels.jDateTimeField(default=timezone.now(), verbose_name='تاریخ')

	def __str__(self):
		print(self.date.date())
		return '{} - {}'.format(self.email,
			self.date.strftime("%y-%m-%d, %H:%M:%S"))

	class Meta:
		verbose_name_plural = 'Contact Us'
