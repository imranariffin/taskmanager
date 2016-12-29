from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.utils import timezone

import datetime

from .models import Task

from .forms import TaskForm

class IndexView(generic.ListView):
	template_name = 'tasks/index.html'
	context_object_name = 'ls_tasks'

	def get_queryset(self):
		ls_tasks = get_list_or_404(Task.objects.order_by('-date_created'))

		return ls_tasks

class DetailView(generic.DetailView):
	model = Task
	template_name = 'tasks/detail.html'

	def get_queryset(self):
		return Task.objects.all()

def create_task(request):

	if request.method == 'POST':
		form = TaskForm(request.POST)

		title = form.data['title']
		description = form.data['description']

		new_task = Task.objects.create(title=title, 
			description=description,
			date_created=timezone.now())
		new_task.save()

		return HttpResponse('posted')

	else:
		form = TaskForm()

	return render(request, 'tasks/create.html', {'form': form})

def edit_task(request, task_id):

	task = get_object_or_404(Task, pk=task_id)

	if request.method == 'POST':
		form = TaskForm(request.POST)

		task.title = form.data['title']
		task.description = form.data['description']

		task.save()

		return HttpResponse('edit')

	else:
		form = TaskForm(instance=task)

	context = {'form': form, 'task': task}
	return render(request, 'tasks/edit.html', context)