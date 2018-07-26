from .models import Film, Theater, Concert
from haystack import indexes
import datetime


class FilmIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField(model_attr='title')
	director = indexes.CharField(model_attr='director')
	producer = indexes.CharField(model_attr='producer')
	release_date = indexes.DateTimeField(model_attr='release_date')
	running_time = indexes.DateTimeField(model_attr='running_time')
	actors = indexes.CharField(model_attr='actors')
	description = indexes.CharField(model_attr='description')
	genre = indexes.CharField(model_attr='genre')
	writer = indexes.CharField(model_attr='writer')

	def get_model(self):
		return Film

	def index_queryset(self, using=None):
		return self.get_model().objects.all()


class TheaterIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField(model_attr='title')
	director = indexes.CharField(model_attr='director')
	producer = indexes.CharField(model_attr='producer')
	running_time = indexes.DateTimeField(model_attr='running_time')
	actors = indexes.CharField(model_attr='actors')
	description = indexes.CharField(model_attr='description')
	genre = indexes.CharField(model_attr='genre')
	writer = indexes.CharField(model_attr='writer')

	def get_model(self):
		return Theater

	def index_queryset(self, using=None):
		return self.get_model().objects.all()


class ConcertIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField(model_attr='title')
	artist = indexes.CharField(model_attr='artist')
	running_time = indexes.DateTimeField(model_attr='running_time')
	description = indexes.CharField(model_attr='description')

	def get_model(self):
		return Concert

	def index_queryset(self, using=None):
		return self.get_model().objects.all()
