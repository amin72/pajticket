from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from braces import views

from . import models as ticket_models
from news import models as news_models
from . import forms


FILM_PRICE = 20000
THEATER_PRICE = 32000
CONCERT_PRICE = 26000


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


class FilmTicketBuyView(views.LoginRequiredMixin,
	generic.DetailView):
	template_name = 'tickets/buy_film_ticket.html'
	form_class = forms.FilmTicket
	model = ticket_models.Film

	def post(self, request, *args, **kwargs):
		film = self.get_object()
		form = self.form_class(request.POST)

		if form.is_valid():
			ticket = form.save(commit=False)
			ticket.user = request.user
			ticket.title = film.title
			ticket.price = FILM_PRICE
			ticket.film = film
			ticket.save()
			request.session['ticket'] = str(ticket)
			return redirect(reverse_lazy('tickets:payment_success'))
		return self.get(request, *args, **kwargs)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context.update(
			{'form': self.form_class(self.request.POST or None)}
		)
		return context


class FilmTicketRemoveView(views.LoginRequiredMixin,
	generic.RedirectView):
	model = ticket_models.FilmTicket

	def get_redirect_url(self, *args, **kwargs):
		return redirect(reverse_lazy('accounts:dashboard'))

	def get_object(self, pk):
		ticket = get_object_or_404(ticket_models.FilmTicket, pk=pk)
		return ticket

	def get(self, request, *args, **kwargs):
		ticket = self.get_object(kwargs.get('pk'))
		ticket.delete()
		return redirect(reverse_lazy('accounts:dashboard'))


class TheaterTicketBuyView(views.LoginRequiredMixin,
	generic.DetailView):
	template_name = 'tickets/buy_theater_ticket.html'
	form_class = forms.TheaterTicket
	model = ticket_models.Theater

	def post(self, request, *args, **kwargs):
		theater = self.get_object()
		form = self.form_class(request.POST)

		if form.is_valid():
			ticket = form.save(commit=False)
			ticket.user = request.user
			ticket.title = theater.title
			ticket.price = THEATER_PRICE
			ticket.theater = theater
			ticket.save()
			request.session['ticket'] = str(ticket)
			return redirect(reverse_lazy('tickets:payment_success'))
		return self.get(request, *args, **kwargs)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context.update(
			{'form': self.form_class(self.request.POST or None)}
		)
		return context


class TheaterTicketRemoveView(views.LoginRequiredMixin,
	generic.RedirectView):
	model = ticket_models.TheaterTicket

	def get_redirect_url(self, *args, **kwargs):
		return redirect(reverse_lazy('accounts:dashboard'))

	def get_object(self, pk):
		ticket = get_object_or_404(ticket_models.TheaterTicket, pk=pk)
		return ticket

	def get(self, request, *args, **kwargs):
		ticket = self.get_object(kwargs.get('pk'))
		ticket.delete()
		return redirect(reverse_lazy('accounts:dashboard'))


class ConcertTicketBuyView(views.LoginRequiredMixin,
	views.FormValidMessageMixin,
	generic.DetailView):
	template_name = 'tickets/buy_concert_ticket.html'
	form_class = forms.ConcertTicket
	model = ticket_models.Concert

	def post(self, request, *args, **kwargs):
		concert = self.get_object()
		form = self.form_class(request.POST)

		if form.is_valid():
			ticket = form.save(commit=False)
			ticket.user = request.user
			ticket.title = concert.title
			ticket.price = CONCERT_PRICE
			ticket.concert = concert
			ticket.place = concert.place
			ticket.save()
			request.session['ticket'] = str(ticket)
			return redirect(reverse_lazy('tickets:payment_success'))
		print(form)
		return self.get(request, *args, **kwargs)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context.update(
			{'form': self.form_class(self.request.POST or None)}
		)
		return context


class ConcertTicketRemoveView(views.LoginRequiredMixin,
	generic.RedirectView):
	model = ticket_models.ConcertTicket

	def get_redirect_url(self, *args, **kwargs):
		return redirect(reverse_lazy('accounts:dashboard'))

	def get_object(self, pk):
		ticket = get_object_or_404(ticket_models.ConcertTicket, pk=pk)
		return ticket

	def get(self, request, *args, **kwargs):
		ticket = self.get_object(kwargs.get('pk'))
		ticket.delete()
		return redirect(reverse_lazy('accounts:dashboard'))


class PaymentSuccess(generic.TemplateView, views.LoginRequiredMixin):
	template_name = 'tickets/payment_success.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['ticket'] = self.request.session.pop('ticket', None)
		return context
