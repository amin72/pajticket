from django.conf.urls import url

from . import views


app_name = 'accounts'

urlpatterns = [
	url(r'^login/$', views.LoginView.as_view(), name='login'),
	url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
	url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
	url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
	
	url(r'^edit/$', views.UserEditView.as_view(), name='user_edit'),
]
