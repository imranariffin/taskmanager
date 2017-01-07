from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

from accounts.forms import RegistrationForm, LoginForm

class RegistrationView(FormView):
	template_name = 'accounts/register.html'
	success_url = '/accounts/login'
	form_class = RegistrationForm

	def form_valid(self, form):

		username = self.request.POST['username']
		password = self.request.POST['password']
		confirm_password = self.request.POST['confirm_password']

		print password

		if password != confirm_password:
			return HttpResponse('Error: Password not match!')

		user = authenticate(
			username=username, 
			password=password)

		if user is None:
			User.objects.create_user(
				username=username,
				password=username).save()

			return HttpResponseRedirect(self.get_success_url())

		return HttpResponse('Error: username oredy exist!')

class LoginView(FormView):
	template_name = 'accounts/login.html'
	success_url = '/tasks'
	form_class = LoginForm

	def form_valid(self,form):
		user = authenticate(
			username=self.request.POST['username'],
			password=self.request.POST['password'])

		if user:
			login(self.request, user)
			return HttpResponseRedirect(self.get_success_url())

		return HttpResponse('Error: fail login!')

def logout_view(request):
	logout(request)

	return HttpResponseRedirect('/tasks')

# test
def user_list(request):
	from django.core import serializers
	user_list = serializers.serialize("json", User.objects.all())

	for user in user_list:
		print user
	print user_list

	from django.http import JsonResponse

	return JsonResponse(user_list, safe=False, content_type="application/json")