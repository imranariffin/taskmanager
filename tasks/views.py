from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

import vanilla

import datetime

from .models import Task

from .forms import TaskForm

# class IndexView(LoginRequiredMixin, generic.ListView):
# 	login_url = '/login/'
# 	redirect_field_name = 'redirect_to'
# 	template_name = 'tasks/index.html'
# 	context_object_name = 'ls_tasks'

# 	def get_queryset(self):
# 		ls_tasks = get_list_or_404(Task.objects.order_by('-date_created'))

# 		return ls_tasks

class IndexView(vanilla.ListView):
	model = Task
	template_name = 'tasks/index.html'

	def get_queryset(self):

		# task_list = get_list_or_404(
		# 	Task.objects.filter(
		# 		user=self.request.user)
		# 	.order_by('-date_created'))

		if not self.request.user.is_authenticated():
			return []

		# try:
		task_list = Task.objects.filter(
			user=self.request.user).order_by('-date_created')
		# except Http404:
		# 	return HttpResponse('user has no task at all')

		return task_list

class DetailView(LoginRequiredMixin, generic.DetailView):
	model = Task
	template_name = 'tasks/detail.html'

	def get_queryset(self):
		return Task.objects.all()

class CreateTask(LoginRequiredMixin, vanilla.CreateView):
	model = Task
	template_name = 'tasks/create.html'
	success_url = '/tasks'
	form_class = TaskForm

	def form_valid(self, form):
		Task.objects.create(
			user=self.request.user,
			title=form.data['title'],
			description=form.data['description'],
			date_created=timezone.now()).save()

		return HttpResponseRedirect(self.get_success_url())

class EditTask(LoginRequiredMixin, vanilla.UpdateView):
	model = Task
	template_name = 'tasks/edit.html'
	success_url = '/tasks'
	form_class = TaskForm

	def form_valid(self, form):
		task = Task.objects.get(id=self.kwargs['pk'])

		task.title = form.data['title']
		task.description = form.data['description']
		task.save()

		return HttpResponseRedirect(self.get_success_url())

	# def get(self, request, *args, **kwargs):
	# 	task = Task.objects.get(id=kwargs['pk'])
	# 	initial = {'title': task.title, 'description': task.description}
	# 	form = self.form_class(initial=initial)

	# 	return render(request, self.template_name, {'form': form})

	# def post(self, request, *args, **kwargs):
	# 	form = self.form_class(request.POST)
	# 	if form.is_valid():
	# 		task = Task.objects.get(id=self.kwargs['pk'])

	# 		task.title = form.data['title']
	# 		task.description = form.data['description']
	# 		task.save()

	# 		return HttpResponseRedirect(self.get_success_url())

	# 	return HttpResponse('fail update')

# task
def all_tasks(request):

	from django.core import serializers

	task_list = serializers.serialize("json", Task.objects.all())

	from django.http import JsonResponse

	return JsonResponse(task_list, safe=False, content_type="application/json")