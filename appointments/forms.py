from django.forms import ModelForm
from django import forms
from .models import Appointment

class AppointmentForm(ModelForm):
	class Meta:
		model = Appointment
		fields = ["name", "description", "appointment_date"]
		widgets = { 'appointment_date': forms.DateTimeInput(attrs={'class': 'datepicker'})}