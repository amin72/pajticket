from django.conf.urls import url

from . import views


app_name = 'tickets'

urlpatterns = [
	url(r'^$', views.HomePageView.as_view(), name='home'),
]
