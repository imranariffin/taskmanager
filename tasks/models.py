from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	description = models.TextField()
	date_created = models.DateTimeField('date created')

	def __str__(self):
		return "<Task: title:{}, user:{}, description:{}> ".format(self.title, self.description, self.user.__str__())

	