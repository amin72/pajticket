from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from reportlab.pdfgen import canvas
from django.http import HttpResponse

from braces import views
from django.http import JsonResponse

from . import models as ticket_models
from news import models as news_models
from . import forms
from advertisements import models as ad_models
from slider import models as slider_models


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
		context['advertisements'] = ad_models.Advertisement.objects.all()[:2]
		slides = slider_models.Slide.objects.all()[:3]

		# check if any of the slides is active		
		active = False
		for slide in slides:
			# if found active slide, make other slides inactive
			if active:
				slide.active = False
				slide.save()
			# if found any active slide, save the state
			if slide.active:
				active = True

		# if no slide is active, make the first one active
		if not active:
			slide = slides[0]
			slide.active = True
			slide.save()

		context['slides'] = slides
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
			request.session['ticket_type'] = 'film'
			request.session['ticket_pk'] = str(ticket.pk)
			return redirect(reverse_lazy('tickets:payment_success'))
		return self.get(request, *args, **kwargs)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context.update({
			'form': self.form_class(self.request.POST or None),
			'price': FILM_PRICE
		})
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
			request.session['ticket_type'] = 'theater'
			request.session['ticket_pk'] = str(ticket.pk)
			return redirect(reverse_lazy('tickets:payment_success'))
		return self.get(request, *args, **kwargs)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context.update({
			'form': self.form_class(self.request.POST or None),
			'price': THEATER_PRICE
		})
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
			request.session['ticket_type'] = 'concert'
			request.session['ticket_pk'] = str(ticket.pk)
			return redirect(reverse_lazy('tickets:payment_success'))
		print(form)
		return self.get(request, *args, **kwargs)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context.update({
			'form': self.form_class(self.request.POST or None),
			'price': CONCERT_PRICE
		})
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
		
		ticket_type = self.request.session.pop('ticket_type', None)
		ticket_pk = self.request.session.pop('ticket_pk', None)

		if ticket_type == 'film':
			ticket = ticket_models.FilmTicket.objects.get(pk=ticket_pk)
		elif ticket_type == 'theater':
			ticket = ticket_models.TheaterTicket.objects.get(pk=ticket_pk)
		elif ticket_type == 'concert':
			ticket = ticket_models.ConcertTicket.objects.get(pk=ticket_pk)
		else:
			ticket = None

		context['ticket'] = ticket
		return context


class ContactUsView(views.LoginRequiredMixin,
	views.FormValidMessageMixin,
	generic.CreateView):

	template_name = 'tickets/contact_us.html'
	form_class = forms.ContactUsForm
	form_valid_message = 'پیام شما با موفقیت ارسال شد'
	success_url = reverse_lazy('tickets:contact_us')

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		obj.save()
		return super().form_valid(form)


def calculate_price(request):
	item_type = request.GET.get('type')
	row = int(request.GET.get('row'))
	
	if item_type == 'film':
		price = FILM_PRICE
	elif item_type == 'theater':
		price = THEATER_PRICE
	elif item_type == 'concert':
		price = CONCERT_PRICE
	else:
		price = 0

	price = ticket_models.calculate_price_by_row(price, row)
	data = {'price': price}
	return JsonResponse(data)
