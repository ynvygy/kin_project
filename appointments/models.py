from django.db import models

# Create your models here.

class Appointment(models.Model):
	name  = models.CharField(max_length=100)
	description = models.TextField(blank=True, max_length=250)
	appointment_date = models.DateTimeField()

	def __str__(self):
		return self.name
