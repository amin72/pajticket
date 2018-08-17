from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from django.http import HttpResponse

from braces import views

from . import models as ticket_models
from news import models as news_models
from . import forms
from advertisements import models as ad_models
from slider import models as slider_models

from .helpers import slide_active, calculate_price
from .helpers import FILM_PRICE, THEATER_PRICE, CONCERT_PRICE


# CreateView: 
# TemplateView: 
# ListView: 
# DetailView:
# LoginRequiredMixin: 
# FormValidMessageMixin:
# RedirectView: 
# REMEMBER pk == id (both are the same)


# home page view
# lists all films, theaters, concerts and news up to 8
# also slides up to 3 and advertisements up to 2
class HomePageView(generic.TemplateView):
	template_name = 'tickets/home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		# get up to 8 films
		context['films'] = ticket_models.Film.objects.all()[:8]
		# get up to 8 theaters
		context['theaters'] = ticket_models.Theater.objects.all()[:8]
		# get up to 8 concerts
		context['concerts'] = ticket_models.Concert.objects.all()[:8]
		# get up to 8 news
		context['news'] = news_models.News.objects.all()[:8]
		# get up to 2 advertisements
		context['advertisements'] = ad_models.Advertisement.objects.all()[:2]

		# get up to 3 slides
		slides = slider_models.Slide.objects.all()[:3]
		# activate slide
		slide_active(slides)
		context['slides'] = slides
		return context


# lists all films in a seperate page
# also advertisements up to 2
class FilmListView(generic.ListView):
	# use Film as our model and list all its elements
	model = ticket_models.Film

	def get_context_data(self, **kwargs):
		# this line gets all films from Film model
		context = super().get_context_data(**kwargs)
		# we just need to add advertisements to the context
		context['advertisements'] = ad_models.Advertisement.objects.all()[:2]
		return context


# show a film detail
class FilmDetailView(generic.DetailView):
	model = ticket_models.Film


# lists all theaters in a seperate page
# also advertisements up to 2
class TheaterListView(generic.ListView):
	# use Theater as our model and list all its elements
	model = ticket_models.Theater

	def get_context_data(self, **kwargs):
		# this line gets all theaters from Theater model
		context = super().get_context_data(**kwargs)
		context['advertisements'] = ad_models.Advertisement.objects.all()[:2]
		return context


# show a theater detail
class TheaterDetailView(generic.DetailView):
	model = ticket_models.Theater


# lists all concerts in a seperate page
# also advertisements up to 2
class ConcerListView(generic.ListView):
	model = ticket_models.Concert

	def get_context_data(self, **kwargs):
		# this line gets all concerts from Concert model
		context = super().get_context_data(**kwargs)
		# we just need to add advertisements to the context
		context['advertisements'] = ad_models.Advertisement.objects.all()[:2]
		return context


# show a Concert detail
class ConcertDetailView(generic.DetailView):
	model = ticket_models.Concert


# Buy a Film ticket
class FilmTicketBuyView(views.LoginRequiredMixin,
	generic.DetailView):
	template_name = 'tickets/buy_film_ticket.html'
	# use FilmTicket as our form
	form_class = forms.FilmTicket
	# use Film as our model
	model = ticket_models.Film

	# user will make post request if buys a ticket
	def post(self, request, *args, **kwargs):
		film = self.get_object()
		form = self.form_class(request.POST)

		if form.is_valid():

			ticket = form.save(commit=False)
			# set ticket's user
			ticket.user = request.user
			# set ticket's title
			ticket.title = film.title
			# set ticket's price
			ticket.price = FILM_PRICE
			# set ticket's film
			ticket.film = film

			# try to get chair number
			try:
				# try to get the last ticket chair_number
				chair_number = \
					ticket_models.FilmTicket.objects.filter(
						film=film, row=ticket.row).last().chair_number
			except AttributeError:
				# if there was not object, set chair_number to 0
				chair_number = 0
			
			# increment chair_number by 1
			ticket.chair_number = chair_number + 1
			# save ticket to database
			ticket.save()
			# set a session for `ticket_type` to `film`
			request.session['ticket_type'] = 'film'
			# set a session for `ticket_pk` to ticket id
			request.session['ticket_pk'] = str(ticket.pk)
			# if successfully created the ticket then redirect to payment_success page
			return redirect(reverse_lazy('tickets:payment_success'))
		return self.get(request, *args, **kwargs)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		# send `form` and `price` to the context
		context.update({
			'form': self.form_class(self.request.POST or None),
			'price': FILM_PRICE
		})
		return context


class FilmTicketRemoveView(views.LoginRequiredMixin,
	generic.RedirectView):
	model = ticket_models.FilmTicket

	# set redirection url
	def get_redirect_url(self, *args, **kwargs):
		return redirect(reverse_lazy('accounts:dashboard'))

	def get_object(self, pk):
		ticket = get_object_or_404(ticket_models.FilmTicket, pk=pk)
		return ticket

	def get(self, request, *args, **kwargs):
		# get film's pk and try to delete it from database
		ticket = self.get_object(kwargs.get('pk'))
		ticket.delete()
		return redirect(reverse_lazy('accounts:dashboard'))


# Buy a Theater ticket
class TheaterTicketBuyView(views.LoginRequiredMixin,
	generic.DetailView):
	template_name = 'tickets/buy_theater_ticket.html'
	# use ThetareTicket as our form
	form_class = forms.TheaterTicket
	# use Theater as our model
	model = ticket_models.Theater

	# user will make post request if buys a ticket
	def post(self, request, *args, **kwargs):
		theater = self.get_object()
		form = self.form_class(request.POST)

		if form.is_valid():
			ticket = form.save(commit=False)
			# set ticket's user
			ticket.user = request.user
			# set ticket's title
			ticket.title = theater.title
			# set ticket's price
			ticket.price = THEATER_PRICE
			ticket.theater = theater

			# try to get chair number
			try:
				# try to get the last ticket chair_number
				chair_number = \
					ticket_models.TheaterTicket.objects.last().chair_number
			except AttributeError:
				# if there was not object, set chair_number to 0
				chair_number = 0

			# increment chair_number by 1		
			ticket.chair_number = chair_number + 1
			# save ticket to database
			ticket.save()
			# set a session for `ticket_type` to `film`
			request.session['ticket_type'] = 'theater'
			# set a session for `ticket_pk` to ticket id
			request.session['ticket_pk'] = str(ticket.pk)
			# if successfully created the ticket then redirect to payment_success page
			return redirect(reverse_lazy('tickets:payment_success'))
		return self.get(request, *args, **kwargs)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		# send `form` and `price` to the context
		context.update({
			'form': self.form_class(self.request.POST or None),
			'price': THEATER_PRICE
		})
		return context


class TheaterTicketRemoveView(views.LoginRequiredMixin,
	generic.RedirectView):
	model = ticket_models.TheaterTicket
	
	# set redirection url
	def get_redirect_url(self, *args, **kwargs):
		return redirect(reverse_lazy('accounts:dashboard'))

	def get_object(self, pk):
		ticket = get_object_or_404(ticket_models.TheaterTicket, pk=pk)
		return ticket

	def get(self, request, *args, **kwargs):
		# get theater's pk and try to delete it from database
		ticket = self.get_object(kwargs.get('pk'))
		ticket.delete()
		return redirect(reverse_lazy('accounts:dashboard'))


# Buy a Concert ticket
class ConcertTicketBuyView(views.LoginRequiredMixin,
	views.FormValidMessageMixin,
	generic.DetailView):
	template_name = 'tickets/buy_concert_ticket.html'
	# use ConcertTicket as our form
	form_class = forms.ConcertTicket
	# use Concert as our model
	model = ticket_models.Concert

	# user will make post request if buys a ticket
	def post(self, request, *args, **kwargs):
		concert = self.get_object()
		form = self.form_class(request.POST)

		if form.is_valid():
			ticket = form.save(commit=False)
			# set ticket's user
			ticket.user = request.user
			# set ticket's title
			ticket.title = concert.title
			# set ticket's price
			ticket.price = CONCERT_PRICE
			ticket.concert = concert
			ticket.place = concert.place

			# try to get chair number
			try:
				# try to get the last ticket chair_number
				chair_number = \
					ticket_models.ConcertTicket.objects.last().chair_number
			except AttributeError:
				# if there was not object, set chair_number to 0
				chair_number = 0

			# increment chair_number by 1		
			ticket.chair_number = chair_number + 1
			# save ticket to database
			ticket.save()
			# set a session for `ticket_type` to `film`
			request.session['ticket_type'] = 'concert'
			# set a session for `ticket_pk` to ticket id
			request.session['ticket_pk'] = str(ticket.pk)
			return redirect(reverse_lazy('tickets:payment_success'))
			# if successfully created the ticket then redirect to payment_success page
		return self.get(request, *args, **kwargs)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		# send `form` and `price` to the context
		context.update({
			'form': self.form_class(self.request.POST or None),
			'price': CONCERT_PRICE
		})
		return context


class ConcertTicketRemoveView(views.LoginRequiredMixin,
	generic.RedirectView):
	model = ticket_models.ConcertTicket

	# set redirection url
	def get_redirect_url(self, *args, **kwargs):
		return redirect(reverse_lazy('accounts:dashboard'))

	def get_object(self, pk):
		ticket = get_object_or_404(ticket_models.ConcertTicket, pk=pk)
		return ticket

	def get(self, request, *args, **kwargs):
		# get concert's pk and try to delete it from database
		ticket = self.get_object(kwargs.get('pk'))
		ticket.delete()
		return redirect(reverse_lazy('accounts:dashboard'))


# when payment was made successfully, it's time to show the user its ticket
# PaymentSuccess class will do the job
# it gets the ticket from database and send it to the context
class PaymentSuccess(generic.TemplateView, views.LoginRequiredMixin):
	template_name = 'tickets/payment_success.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		# get the `ticket_type` from session
		ticket_type = self.request.session.pop('ticket_type', None)
		# get the `ticket_pk` from session
		ticket_pk = self.request.session.pop('ticket_pk', None)


		# deppend on the ticket type get the ticket with the specified id
		# and send it to the context
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


# will control concat us page and form
class ContactUsView(views.FormValidMessageMixin, generic.CreateView):
	template_name = 'tickets/contact_us.html'
	# use ContactUsForm to get users' suggestions
	form_class = forms.ContactUsForm
	# if form submition was valid, show this message to user
	form_valid_message = 'پیام شما با موفقیت ارسال شد'
	# redirect to this url after form submittion
	success_url = reverse_lazy('tickets:contact_us')
