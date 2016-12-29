from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from tasks.models import Task

# Create your tests here.
class TaskTestCase(TestCase):
	def setUp(self):
		Task.objects.create(title='Recent Task A',
			description='A recent task',
			date_created=timezone.now())

		Task.objects.create(title='Future Task B',
			description='A future task',
			date_created=timezone.now() + timedelta(days=30))

	# def 