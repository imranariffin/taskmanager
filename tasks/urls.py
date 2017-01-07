from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'tasks'
urlpatterns = [
	# test
	url(r'^all/$', views.all_tasks, name='all_tasks'),
	
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^create/$', views.CreateTask.as_view(), name='create'),
	url(r'^(?P<pk>[0-9]+)/edit/$', views.EditTask.as_view(), name='edit'),
]
