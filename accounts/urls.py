from django.conf.urls import url

from . import views

app_name = 'accounts'
urlpatterns = [
	url(r'^register/', views.RegistrationView.as_view(), name='register'),
	url(r'^login/', views.LoginView.as_view(), name='login'),
	url(r'^logout/', views.logout_view, name='logout'),

	# test
	url(r'^users/', views.user_list, name='users'),
]
