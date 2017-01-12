from django import forms
from django.contrib.auth.models import User
from .models import Task

class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ('title', 'description')

	# title = forms.CharField(label='Title', max_length=200)
	# description = forms.CharField(label='Description', max_length=800)

class TaskDeleteForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ('title',)