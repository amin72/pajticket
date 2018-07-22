from django.shortcuts import render
from django.views import generic

from braces import views

from .models import News


class NewsListView(generic.ListView):
	template_name = 'news/news_list.html'
	model = News


class NewsDetailView(generic.DetailView):
	template_name = 'news/news_detail.html'
	model = News
