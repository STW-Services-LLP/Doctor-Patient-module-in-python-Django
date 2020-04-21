from django.shortcuts import render
from django.shortcuts import get_object_or_404
from doctor.models import doctor
from appointment.models import Appointment_Booking
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url = 'login')
def appointment(request):
	dep = doctor.objects.all()
	if request.method == 'POST':
		first_name = request.POST['first-name']
		last_name = request.POST['last-name']
		phone = request.POST['phone']
		email = request.POST['email']
		address = request.POST['address']
		city = request.POST['city']
		your_schedule = request.POST['your-schedule']
		date =request.POST['date']
		doctor_name = request.POST['doctor-name']
		country = request.POST['country']
		your_message = request.POST['message']
		
		new_object = Appointment_Booking.objects.create(first_name = first_name ,last_name = last_name , phone = phone,email = email , address = address , city = city , schedule_time = your_schedule ,doctor_name = doctor_name,country = country ,description = your_message ,appointment = date)
		new_object.save()
		return HttpResponse('Sent Successfully!!')
	else:	
		return render(request ,'appointment.html',{"depart":dep})
@login_required(login_url = 'login')
def appointment_request(request):
	appoint = Appointment_Booking.objects.all()
	return render(request, 'appointment_request.html',{"appoint":appoint})

def appointment_details(request , id):
	app = Appointment_Booking.objects.get(id=id)
	return render(request, 'appointment_details.html',{"app":app})