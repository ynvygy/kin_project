from django.shortcuts import render, redirect
from .forms import AppointmentForm

# Create your views here.

def homepage(request):
	return render(request, 'appointments/homepage.html', {'title': "Welcome to Kin's page"})

def set_appointment(request):
	if request.method == "GET":
		return render(request, 'appointments/set_appointment.html', {'form': AppointmentForm()})
	else:
		form = AppointmentForm(request.POST)
		form.save()
		return redirect('thank_you')

def thank_you(request):
	return render(request, 'appointments/thank_you.html')