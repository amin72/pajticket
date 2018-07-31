from .models import Film, Theater, Concert
from haystack import indexes
import datetime


class FilmIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField(model_attr='title')

	def get_model(self):
		return Film

	def index_queryset(self, using=None):
		return self.get_model().objects.all()


class TheaterIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField(model_attr='title')

	def get_model(self):
		return Theater

	def index_queryset(self, using=None):
		return self.get_model().objects.all()


class ConcertIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField(model_attr='title')

	def get_model(self):
		return Concert

	def index_queryset(self, using=None):
		return self.get_model().objects.all()


class DirectorIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField(model_attr='title')

	def get_model(self):
		return Concert

	def index_queryset(self, using=None):
		return self.get_model().objects.all()
