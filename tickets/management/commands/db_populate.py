from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User

import random
from tickets.models import (Country, People, Language, Genre,
							Actor, Director, Producer, Writer, Film,
							Theater, Song, Concert, Place)

from news.models import News


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
	dict(title='سریع و خشن ۱', release_date=timezone.datetime(2001, 3, 5), running_time=timezone.datetime(2018, 8, 28), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۲', release_date=timezone.datetime(2003, 3, 5), running_time=timezone.datetime(2018, 8, 25), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۳', release_date=timezone.datetime(2005, 3, 5), running_time=timezone.datetime(2018, 9, 15), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۴', release_date=timezone.datetime(2007, 3, 5), running_time=timezone.datetime(2018, 8, 29), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۵', release_date=timezone.datetime(2009, 3, 5), running_time=timezone.datetime(2018, 3, 15), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۶', release_date=timezone.datetime(2011, 3, 5), running_time=timezone.datetime(2018, 8, 24), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۷', release_date=timezone.datetime(2013, 3, 5), running_time=timezone.datetime(2018, 8, 15), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۸', release_date=timezone.datetime(2015, 3, 5), running_time=timezone.datetime(2018, 8, 25), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۹', release_date=timezone.datetime(2015, 3, 5), running_time=timezone.datetime(2018, 7, 30), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
]

theaters = [
	dict(title='داماد دیوانه ۱', running_time=timezone.datetime(2015, 3, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='داماد دیوانه ۲', running_time=timezone.datetime(2015, 3, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='داماد دیوانه ۳', running_time=timezone.datetime(2015, 3, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='داماد دیوانه ۴', running_time=timezone.datetime(2015, 3, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='داماد دیوانه ۵', running_time=timezone.datetime(2015, 3, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='داماد دیوانه ۶', running_time=timezone.datetime(2015, 3, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
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
	dict(title='کنسرت رضا صادقی', artist=reza_sadeghi, place=Place.objects.create(name='خیابان آزادی'), length=60, running_time=timezone.datetime(2018, 8, 10), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='کنسرت علی لهراسبی', artist=ali_lohrasbi, place=Place.objects.create(name='پارک ولیعصر'), length=100, running_time=timezone.datetime(2018, 9, 25), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
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
	dict(name='سینما فرهنگ'),
	dict(name='سینما مرکزی'),
	dict(name='سینما شکوفه'),
	dict(name='سینما آفریقا'),
	dict(name='سینما بهمن'),
	dict(name='سینما قدس'),
	dict(name='سینما ایران'),
	dict(name='سینما ملت'),
	dict(name='سینما حافظ'),
	dict(name='سینما استقلال'),
	dict(name='سینما پردیس'),
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

   		_producers = [ Producer.objects.create(person=p) for p in _people[: len(people)//2 ] ]
   		print("Populated producers table")

    	# create some writers
   		_writers = [ Writer.objects.create(person=p) for p in _people[len(people)//2:] ]
   		print("Populated writers table")

   		for film in films:
   			director = random.choice(_directors)
   			producer = random.choice(_producers)
   			actors = random.sample(_actors, 5)
   			writer = random.choice(_writers)
   			genre = random.choice(_genres)
   			country = random.choice(_countries)
   			language = _languages[0]
   			Film.objects.create(**film, director=director, producer=producer,
   				writer=writer, genre=genre, country=country, language=language)
   		print("Populated films table")


   		for theater in theaters:
   			director = random.choice(_directors)
   			actors = random.sample(_actors, 5)
   			writer = random.choice(_writers)
   			genre = random.choice(_genres)
   			Theater.objects.create(**theater, director=director, writer=writer, genre=genre)
   		print("Populated theaters table")


   		_songs = [Song.objects.create(**s) for s in songs]
   		print("Populated songs table")


   		_concerts = [Concert.objects.create(**c) for c in concerts]
   		# for concert in concerts:
   		# 	song = random.choice(_songs)
   		# 	title = 'کنسرت '.format(song.singer)
   		# 	Concert.objects.create(**concert)
   		print("Populated concerts table")
