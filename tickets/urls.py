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

	url(r'^buy/$', views.BuyTicketView.as_view(), name='buy_ticket'),
	
	# url(r'^payment/$', views.PaymentView.as_view(), name='payment'),	
	
]
