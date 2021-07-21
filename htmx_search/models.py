from django.db import models

# Create your models here.

class Clients(models.Model):
	first_name = models.CharField(max_length=200, blank=True)
	last_name = models.CharField(max_length=200, blank=True)
	email = models.EmailField(max_length=200, blank=True)

	def __str__(self):
		return f'{self.first_name} - {self.last_name}'