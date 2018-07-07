from django.conf.urls import url

from . import views


app_name = 'accounts'

urlpatterns = [
	url(r'^$', views.LoginView.as_view(), name='login'),
	url(r'^$', views.SignUpView.as_view(), name='signup'),
	url(r'^$', views.LogoutView.as_view(), name='signup'),
	url(r'^$', views.DashboardView.as_view(), name='dashboard'),
]
