from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Task(models.Model):
	title = models.CharField(max_length=200)
	overview = models.TextField(blank=True, null=True)
	completed = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(
		User, on_delete=models.CASCADE, null=True, blank=True
		)

	def __str__(self):
		return f'{self.title} by {self.user}'

	def get_absolute_url(self):
		return reverse('task_detail', args=(str(self.pk)))