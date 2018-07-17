from django.shortcuts import render
from django.views import generic

from . import models as ticket_models
from news import models as news_models



class HomePageView(generic.TemplateView):
	template_name = 'tickets/home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['films'] = ticket_models.Film.objects.all()[:8]
		context['theaters'] = ticket_models.Theater.objects.all()[:8]
		context['concerts'] = ticket_models.Concert.objects.all()[:8]
		context['news'] = news_models.News.objects.all()[:8]
		return context



class FilmListView(generic.ListView):
	model = ticket_models.Film



class FilmDetailView(generic.DetailView):
	model = ticket_models.Film



class TheaterListView(generic.ListView):
	model = ticket_models.Theater



class TheaterDetailView(generic.DetailView):
	model = ticket_models.Theater



class ConcerListView(generic.ListView):
	model = ticket_models.Concert



class ConcertDetailView(generic.DetailView):
	model = ticket_models.Concert



class BuyTicketView(generic.TemplateView):
	template_name = 'tickets/buyticket.html'
	