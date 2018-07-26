from django.conf.urls import url

from . import views


app_name = 'tickets'

urlpatterns = [
	url(r'^$', views.HomePageView.as_view(), name='home'),
	
	url(r'^films/$', views.FilmListView.as_view(), name='films'),
	
	url(r'^films/(?P<pk>\d+)/$', views.FilmDetailView.as_view(),
		name='film_detail'),
	
	url(r'^theaters/$', views.TheaterListView.as_view(), name='theaters'),
	
	url(r'^theaters/(?P<pk>\d+)/$', views.TheaterDetailView.as_view(),
		name='theater_detail'),

	url(r'^concerts/$', views.ConcerListView.as_view(), name='concerts'),

	url(r'^concerts/(?P<pk>\d+)/$', views.ConcertDetailView.as_view(),
		name='concert_detail'),

	# buy film ticket
	url(r'^films/(?P<pk>\d+)/buy/$', views.FilmTicketBuyView.as_view(),
		name='buy_film_ticket'),

	# buy theater ticket
	url(r'^theaters/(?P<pk>\d+)/buy/$', views.TheaterTicketBuyView.as_view(),
		name='buy_theater_ticket'),

	# buy concert ticket
	url(r'^concerts/(?P<pk>\d+)/buy/$', views.ConcertTicketBuyView.as_view(),
		name='buy_concert_ticket'),

	# remove film ticket
	url(r'^films/(?P<pk>\d+)/remove/$', views.FilmTicketRemoveView.as_view(),
		name='remove_film_ticket'),

	# remove theater ticket
	url(r'^theaters/(?P<pk>\d+)/remove/$',
		views.TheaterTicketRemoveView.as_view(),
		name='remove_theater_ticket'),

	# remove concert ticket
	url(r'^concerts/(?P<pk>\d+)/remove/$',
		views.ConcertTicketRemoveView.as_view(),
		name='remove_concert_ticket'),

	# payment_success
	url(r'^payment_success/$', views.PaymentSuccess.as_view(),
		name='payment_success'),

	# contact us
	url(r'^contact_us/$', views.ContactUsView.as_view(),
		name='contact_us'),	

	# calculate_price
	url(r'^calculate_price/$', views.calculate_price,
		name='calculate_price'),
]
