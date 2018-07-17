from django.core.management.base import BaseCommand
from django.utils import timezone
import random
from tickets.models import (Country, People, Language, Genre,
							Actor, Director, Writer, Film, Theater,
							Song, Concert)

from news.models import News


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
	dict(first_name='امین', last_name='امینی', gender='m', birth_day=timezone.datetime(2000, 1, 20)),
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
	dict(title='سریع و خشن ۱', release_time=timezone.datetime(2001, 3, 5), runnig_time=timezone.datetime(2001, 3, 15), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۲', release_time=timezone.datetime(2003, 3, 5), runnig_time=timezone.datetime(2003, 3, 15), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۳', release_time=timezone.datetime(2005, 3, 5), runnig_time=timezone.datetime(2005, 3, 15), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۴', release_time=timezone.datetime(2007, 3, 5), runnig_time=timezone.datetime(2007, 3, 15), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۵', release_time=timezone.datetime(2009, 3, 5), runnig_time=timezone.datetime(2009, 3, 15), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۶', release_time=timezone.datetime(2011, 3, 5), runnig_time=timezone.datetime(2011, 3, 15), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۷', release_time=timezone.datetime(2013, 3, 5), runnig_time=timezone.datetime(2013, 3, 15), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='سریع و خشن ۸', release_time=timezone.datetime(2015, 3, 5), runnig_time=timezone.datetime(2015, 3, 15), length=120, description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
]

theaters = [
	dict(title='داماد دیوانه ۱', runnig_time=timezone.datetime(2015, 3, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='داماد دیوانه ۲', runnig_time=timezone.datetime(2015, 3, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='داماد دیوانه ۳', runnig_time=timezone.datetime(2015, 3, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='داماد دیوانه ۴', runnig_time=timezone.datetime(2015, 3, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='داماد دیوانه ۵', runnig_time=timezone.datetime(2015, 3, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='داماد دیوانه ۶', runnig_time=timezone.datetime(2015, 3, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
]

songs = [
	dict(title='پیراهن سیاه ۱', length=8),
	dict(title='پیراهن سیاه ۲', length=14),
	dict(title='پیراهن سیاه ۳', length=8),
	dict(title='پیراهن سیاه ۴', length=7),
	dict(title='پیراهن سیاه ۵', length=9),
	dict(title='پیراهن سیاه ۶', length=11),
	dict(title='عشق ۱', length=11),
	dict(title='عشق ۲', length=10),
	dict(title='عشق ۳', length=15),
]

concerts = [
	dict(title='کنسرت رضا صادقی', date=timezone.datetime(2018, 5, 10), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='کنسرت علی لهراسبی', date=timezone.datetime(2018, 6, 20), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
]


news = [
	dict(title='اسامی فیلم‌های خارجی بخش «جشنواره جشنواره‌ها» اعلام شد/ فیلم‌هایی از آمریکای جنوبی و اروپا در فهرست هستند', date=timezone.datetime(2018, 5, 1), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='اسامی فیلم‌های خارجی بخش «جشنواره جشنواره‌ها» اعلام شد/ فیلم‌هایی از آمریکای جنوبی و اروپا در فهرست هستند', date=timezone.datetime(2018, 5, 2), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='اسامی فیلم‌های خارجی بخش «جشنواره جشنواره‌ها» اعلام شد/ فیلم‌هایی از آمریکای جنوبی و اروپا در فهرست هستند', date=timezone.datetime(2018, 5, 5), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='اسامی فیلم‌های خارجی بخش «جشنواره جشنواره‌ها» اعلام شد/ فیلم‌هایی از آمریکای جنوبی و اروپا در فهرست هستند', date=timezone.datetime(2018, 5, 9), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='اسامی فیلم‌های خارجی بخش «جشنواره جشنواره‌ها» اعلام شد/ فیلم‌هایی از آمریکای جنوبی و اروپا در فهرست هستند', date=timezone.datetime(2018, 5, 10), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='اسامی فیلم‌های خارجی بخش «جشنواره جشنواره‌ها» اعلام شد/ فیلم‌هایی از آمریکای جنوبی و اروپا در فهرست هستند', date=timezone.datetime(2018, 5, 15), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
	dict(title='اسامی فیلم‌های خارجی بخش «جشنواره جشنواره‌ها» اعلام شد/ فیلم‌هایی از آمریکای جنوبی و اروپا در فهرست هستند', date=timezone.datetime(2018, 5, 21), description='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
]

class Command(BaseCommand):
    def handle(self, count=20, *args, **options):
    	# create some news
   		_news = [ News.objects.create(**n) for n in news ]
   		print("Populated news table")

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

    	# create some writers
   		_writers = [ Writer.objects.create(person=p) for p in _people[len(people)//2:] ]
   		print("Populated writers table")

   		for film in films:
   			director = random.choice(_directors)
   			actors = random.sample(_actors, 5)
   			writer = random.choice(_writers)
   			genre = random.choice(_genres)
   			country = random.choice(_countries)
   			language = _languages[0]
   			Film.objects.create(**film, director=director, writer=writer, genre=genre, country=country, language=language)
   		print("Populated films table")


   		for theater in theaters:
   			director = random.choice(_directors)
   			actors = random.sample(_actors, 5)
   			writer = random.choice(_writers)
   			genre = random.choice(_genres)
   			Theater.objects.create(**theater, director=director, writer=writer, genre=genre)
   		print("Populated theaters table")


   		_songs = []
   		for song in songs:
   			singer = random.choice(_people)
   			_songs.append(Song.objects.create(**song, singer=singer))
   		print("Populated songs table")


   		for concert in concerts:
   			artist = random.choice(_songs).singer
   			Concert.objects.create(**concert, artist=artist)
   		print("Populated concerts table")
