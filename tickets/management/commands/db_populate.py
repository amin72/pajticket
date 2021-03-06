from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User

import random
from datetime import datetime
from tickets.models import (Country, People, Language, Genre,
							Actor, Director, Producer, Writer, Film,
							Theater, Song, Concert, Place)

from advertisements.models import Advertisement
from news.models import News
from slider.models import Slide

import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

users = [
	dict(username='amin', password='amin1234', email='amin@example.com', first_name='امین', last_name='امینی'),
	dict(username='ali', password='ali1234', email='ali@exampple.com', first_name='علی', last_name='علوی'),
	dict(username='hamid', password='hamid1234', email='hamid@example.com', first_name='حمید', last_name='حمیدی'),
	dict(username='maryam', password='maryam1234', email='maryam@example.com', first_name='مریم', last_name='رضایی'),
	dict(username='reza', password='reza1234', email='reza@example.com', first_name='رضا', last_name='رضایی'),
	dict(username='zahra', password='zahra1234', email='zahra@example.com', first_name='زهرا', last_name='فاطمی'),
]

counties = [
	dict(name='آمریکا'),
	dict(name='انگلستان'),
	dict(name='کانادا'),
	dict(name='برزیل'),
	dict(name='ایران'),
	dict(name='امارات'),
	dict(name='ژاپن'),
	dict(name='کره'),
	dict(name='مصر'),
	dict(name='کویت'),
	dict(name='فرانسه'),
	dict(name='آلمان'),
]

languages = [
	dict(name='فارسی'),
	dict(name='انگلیسی'),
	dict(name='چینی'),
	dict(name='عربی'),
	dict(name='ترکی'),
	dict(name='فرانوسی'),
	dict(name='آلمانی'),
	dict(name='کره ای'),
	dict(name='ژاپنی'),
]

genres = [
	dict(title='اکشن'),
	dict(title='درام'),
	dict(title='کمدی'),
]

people = [
	dict(first_name='امیر', last_name='امیری', gender='m', birth_day=timezone.datetime(2000, 1, 20)),
	dict(first_name='علی', last_name='علوی', gender='m', birth_day=timezone.datetime(2000, 1, 20)),
	dict(first_name='رضا', last_name='کریمی', gender='m', birth_day=timezone.datetime(2000, 1, 20)),
	dict(first_name='حمید', last_name='حسنی', gender='m', birth_day=timezone.datetime(2000, 1, 20)),
	dict(first_name='محمد', last_name='رضایی', gender='m', birth_day=timezone.datetime(2000, 1, 20)),
	dict(first_name='امیر', last_name='محمدی', gender='m', birth_day=timezone.datetime(2000, 1, 20)),
	dict(first_name='رضا', last_name='امیدی', gender='m', birth_day=timezone.datetime(2000, 1, 20)),
	dict(first_name='زهرا', last_name='نوایی', gender='f', birth_day=timezone.datetime(2000, 1, 20)),
	dict(first_name='امید', last_name='حمیدی', gender='m', birth_day=timezone.datetime(2000, 1, 20)),
	dict(first_name='مینو', last_name='کریمی', gender='f', birth_day=timezone.datetime(2000, 1, 20)),
	dict(first_name='حسن', last_name='امینی', gender='m', birth_day=timezone.datetime(2000, 1, 20)),
	dict(first_name='زینب', last_name='محمدی', gender='f', birth_day=timezone.datetime(2000, 1, 20)),
	dict(first_name='فاطمه', last_name='امینی', gender='f', birth_day=timezone.datetime(2000, 1, 20)),
	dict(first_name='نقی', last_name='هاشمی', gender='m', birth_day=timezone.datetime(2000, 1, 20)),
	dict(first_name='مریم', last_name='امیری', gender='f', birth_day=timezone.datetime(2000, 1, 20)),
	dict(first_name='مهرنوش', last_name='فاطمی', gender='f', birth_day=timezone.datetime(2000, 1, 20)),
]

films = [
	dict(title='سریع و خشن ۱', cover='images/films/01.jpg', release_date=timezone.datetime(2001, 3, 5).date(), running_time=timezone.datetime(2018, 8, 28, 16, 30), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۲', cover='images/films/02.jpg', release_date=timezone.datetime(2003, 3, 5).date(), running_time=timezone.datetime(2018, 8, 25, 21), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۳', cover='images/films/03.jpg', release_date=timezone.datetime(2005, 3, 5).date(), running_time=timezone.datetime(2018, 9, 15, 22, 30), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۴', cover='images/films/04.jpg', release_date=timezone.datetime(2007, 3, 5).date(), running_time=timezone.datetime(2018, 8, 29, 15, 30), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۵', cover='images/films/05.jpg', release_date=timezone.datetime(2009, 3, 5).date(), running_time=timezone.datetime(2018, 3, 15, 18), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۶', cover='images/films/06.jpg', release_date=timezone.datetime(2011, 3, 5).date(), running_time=timezone.datetime(2018, 8, 24, 21), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۷', cover='images/films/07.jpg', release_date=timezone.datetime(2013, 3, 5).date(), running_time=timezone.datetime(2018, 8, 15, 17, 30), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۸', cover='images/films/08.jpg', release_date=timezone.datetime(2015, 3, 5).date(), running_time=timezone.datetime(2018, 8, 25, 22, 30), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۹', cover='images/films/09.jpg', release_date=timezone.datetime(2015, 3, 5).date(), running_time=timezone.datetime(2018, 7, 30, 18), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۱۰', cover='images/films/10.jpg', release_date=timezone.datetime(2020, 6, 12).date(), running_time=timezone.datetime(2020, 7, 30, 15, 30), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
]

theaters = [
	dict(title='داماد دیوانه ۱', cover='images/theaters/01.jpg', length=215, running_time=timezone.datetime(2015, 3, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='داماد دیوانه ۲', cover='images/theaters/02.jpg', length=215, running_time=timezone.datetime(2015, 3, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='داماد دیوانه ۳', cover='images/theaters/03.jpg', length=215, running_time=timezone.datetime(2015, 3, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='داماد دیوانه ۴', cover='images/theaters/04.jpg', length=215, running_time=timezone.datetime(2015, 3, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='داماد دیوانه ۵', cover='images/theaters/05.jpg', length=215, running_time=timezone.datetime(2015, 3, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='داماد دیوانه ۶', cover='images/theaters/06.jpg', length=215, running_time=timezone.datetime(2015, 3, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='داماد دیوانه ۷', cover='images/theaters/07.jpg', length=215, running_time=timezone.datetime(2015, 3, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='داماد دیوانه ۸', cover='images/theaters/08.jpg', length=215, running_time=timezone.datetime(2015, 3, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
]

reza_sadeghi = People.objects.create(first_name='رضا', last_name='صادقی', gender='m', birth_day=timezone.datetime(1980, 1, 28))
ali_lohrasbi = People.objects.create(first_name='علی', last_name='لهراسبی', gender='m', birth_day=timezone.datetime(1982, 5, 12))

songs = [
	dict(title='پیراهن سیاه ۱', length=8, singer=reza_sadeghi),
	dict(title='پیراهن سیاه ۲', length=14, singer=reza_sadeghi),
	dict(title='پیراهن سیاه ۳', length=8, singer=reza_sadeghi),
	dict(title='پیراهن سیاه ۴', length=7, singer=reza_sadeghi),
	dict(title='پیراهن سیاه ۵', length=9, singer=reza_sadeghi),
	dict(title='پیراهن سیاه ۶', length=11, singer=reza_sadeghi),
	dict(title='عشق ۱', length=11, singer=ali_lohrasbi),
	dict(title='عشق ۲', length=10, singer=ali_lohrasbi),
	dict(title='عشق ۳', length=15, singer=ali_lohrasbi),
]

concerts = [
	dict(title='کنسرت رضا صادقی', cover='images/concerts/01.jpg', artist=reza_sadeghi, place=Place.objects.create(name='سینما آزادی', address='تهران - خیابان آزادی'), length=60, running_time=timezone.datetime(2018, 8, 10), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='کنسرت علی لهراسبی', cover='images/concerts/02.jpg', artist=ali_lohrasbi, place=Place.objects.create(name='پارک ولیعصر', address='تهران - خیابان ولیعصر'), length=100, running_time=timezone.datetime(2018, 9, 25), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
]

news = [
	dict(title='اسامی فیلم‌های خارجی بخش «جشنواره جشنواره‌ها» اعلام شد/ فیلم‌هایی از آمریکای جنوبی و اروپا در فهرست هستند', text='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='اسامی فیلم‌های خارجی بخش «جشنواره جشنواره‌ها» اعلام شد/ فیلم‌هایی از آمریکای جنوبی و اروپا در فهرست هستند', text='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='اسامی فیلم‌های خارجی بخش «جشنواره جشنواره‌ها» اعلام شد/ فیلم‌هایی از آمریکای جنوبی و اروپا در فهرست هستند', text='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='اسامی فیلم‌های خارجی بخش «جشنواره جشنواره‌ها» اعلام شد/ فیلم‌هایی از آمریکای جنوبی و اروپا در فهرست هستند', text='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='اسامی فیلم‌های خارجی بخش «جشنواره جشنواره‌ها» اعلام شد/ فیلم‌هایی از آمریکای جنوبی و اروپا در فهرست هستند', text='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='اسامی فیلم‌های خارجی بخش «جشنواره جشنواره‌ها» اعلام شد/ فیلم‌هایی از آمریکای جنوبی و اروپا در فهرست هستند', text='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='اسامی فیلم‌های خارجی بخش «جشنواره جشنواره‌ها» اعلام شد/ فیلم‌هایی از آمریکای جنوبی و اروپا در فهرست هستند', text='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
]

places = [
	dict(name='سینما فرهنگ', address='تهران - خیابان فرهنگ'),
	dict(name='سینما مرکزی', address='تهران - خیابان مرکزی'),
	dict(name='سینما شکوفه', address='تهران - خیابان شکوفه'),
	dict(name='سینما آفریقا', address='تهران - خیابان آفریقا'),
	dict(name='سینما بهمن', address='تهران - خیابان بهمن'),
	dict(name='سینما قدس', address='تهران - خیابان قدس'),
	dict(name='سینما ایران', address='تهران - خیابان ایران'),
	dict(name='سینما ملت', address='تهران - خیابان ملت'),
	dict(name='سینما حافظ', address='تهران - خیابان حافظ'),
	dict(name='سینما استقلال', address='تهران - خیابان استقلال'),
	dict(name='سینما پردیس', address='تهران - خیابان پردیس'),
]

advertisements = [
	dict(image='images/advertisements/ad01.jpg', url='http://www.google.com', order=1),
	dict(image='images/advertisements/ad02.jpg', url='http://www.yahoo.com', order=2),
]

slides = [
	dict(image='images/slider/01.jpg', url='http://www.google.com', order=1),
	dict(image='images/slider/02.jpg', url='http://www.yahoo.com', order=2),
	dict(image='images/slider/03.jpg', url='http://www.python.org', order=3),
]


class Command(BaseCommand):
    def handle(self, count=20, *args, **options):
    	# create some news
   		_news = [ News.objects.create(**n) for n in news ]
   		print("Populated news table")

   		# create some users
   		_users = []
   		for u in users:
   			password = u.pop('password')
   			user = User.objects.create(**u)
   			user.set_password(password)
   			user.save()
   			_users.append(user)
   		print('Populated users tables')

		# create some places
   		_places = [ Place.objects.create(**p) for p in places ]
   		print("Populated places table")

    	# create some countries
   		_countries = [ Country.objects.create(**c) for c in counties ]
   		print("Populated counties table")

    	# create some languages
   		_languages = [ Language.objects.create(**l) for l in languages ]
   		print("Populated languages table")

    	# create some languages
   		_genres = [ Genre.objects.create(**g) for g in genres ]
   		print("Populated genres table")

    	# create some people
   		_people = [ People.objects.create(**p) for p in people ]
   		print("Populated people table")

    	# create some actors
   		_actors = [ Actor.objects.create(person=p) for p in _people ]
   		print("Populated actors table")

    	# create some directors
   		_directors = [ Director.objects.create(person=p) for p in _people[: len(people)//2 ] ]
   		print("Populated directors table")

   		# create some produsers
   		_producers = [ Producer.objects.create(person=p) for p in _people[: len(people)//2 ] ]
   		print("Populated producers table")

    	# create some writers
   		_writers = [ Writer.objects.create(person=p) for p in _people[len(people)//2:] ]
   		print("Populated writers table")

   		# create some films
   		for film in films:
   			director = random.choice(_directors)
   			producer = random.choice(_producers)
   			actors = random.sample(_actors, 5)
   			writer = random.choice(_writers)
   			genre = random.choice(_genres)
   			country = random.choice(_countries)
   			language = random.choice(_languages)
   			Film.objects.create(**film, director=director, producer=producer,
   				writer=writer, genre=genre, country=country, language=language)
   		print("Populated films table")

   		# create some theaters
   		for theater in theaters:
   			director = random.choice(_directors)
   			producer = random.choice(_producers)
   			actors = random.sample(_actors, 5)
   			writer = random.choice(_writers)
   			genre = random.choice(_genres)
   			language = random.choice(_languages)
   			Theater.objects.create(**theater, director=director, language=language, producer=producer, writer=writer, genre=genre)
   		print("Populated theaters table")

   		# create some songs
   		_songs = [Song.objects.create(**s) for s in songs]
   		print("Populated songs table")

   		# create some concerts
   		_concerts = [Concert.objects.create(**c) for c in concerts]
   		# for concert in concerts:
   		# 	song = random.choice(_songs)
   		# 	title = 'کنسرت '.format(song.singer)
   		# 	Concert.objects.create(**concert)
   		print("Populated concerts table")

   		# create some advertisements
   		_ads = [Advertisement.objects.create(**ad) for ad in advertisements]

   		# create some slides
   		_slides = [Slide.objects.create(**s) for s in slides]
