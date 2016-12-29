from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Task(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	date_created = models.DateTimeField('date created')

	def __str__(self):
		return "<Task: title:{}, description:{}> ".format(self.title, self.description)

	