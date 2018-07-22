from django.conf.urls import url

from . import views


app_name = 'news'

urlpatterns = [
	# news list
	url(r'^$', views.NewsListView.as_view(), name='list'),

	# news detail
	url(r'^detail/(?P<pk>\d+)/$', views.NewsDetailView.as_view(),
		name='detail'),
]