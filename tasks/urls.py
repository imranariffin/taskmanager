from django.conf.urls import url

from . import views, auth_views

app_name = 'tasks'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^create/$', views.create_task, name='create'),
	url(r'^(?P<task_id>[0-9]+)/edit/$', views.edit_task, name='edit'),
]
