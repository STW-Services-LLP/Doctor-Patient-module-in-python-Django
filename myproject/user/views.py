from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import CustomUser
from .models import Doctor

# Create your views here.
# @receiver(post_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		if instance.is_patient:
# 			Patient.objects.create(user=instance)
# 		elif instance.is_doctor:
# 			Doctor.objects.create(user=instance)

# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
# 	if instance.is_patient:
# 		instance.patient.save()
# 	elif instance.is_doctor:
# 		instance.doctor.save()		
def register(request):
	
	if request.method=='POST':
		form1 = RegisterForm(request.POST)
		if form1.is_valid():
			form1.save()
			login(self.request, user)
		return redirect('/')	
	else:
		form1 = RegisterForm()
	return render(request,"signup.html",{"form1":form1})



# def login(request):

# 	if request.method=='POST':
# 	 	form = LoginForm(request.POST)
# 	 	if form.is_valid():
# 	 		return redirect('/')
	 	
# 	else:
# 	 	form = LoginForm()
# 	return render(request,"registration/login.html",{"form":form})
# def SignUp(request):
# 	if request.method=="POST":
# 		username = request.POST['username']
# 		firstname = request.POST['first_name']
# 		lastname = request.POST['last_name']
# 		email = request.POST['email_id']
# 		password = request.POST['password']
# 		x = User.objects.create(username = username ,first_name = firstname ,last_name = lastname ,email = email, password = password )
# 		x.save()
# 		return HttpResponse('Hello, World!')
# 		return redirect('')
# 	else:	
# 	    return render(request,"signup.html")

# def Login(request):
# 	if request.method=='POST':
# 		username1 = request.POST['username']
# 		password1 = request.POST['password']
# 		x = authenticate(username=username1 ,password=password1)
# 		if x is not None:
# 			return HttpResponse('loginss')
# 			# return redirect('login')
# 		else:
# 			return HttpResponse('LOGIN FAILED')
			
# 			# return redirect('signup')

# 	else:	
# 		return render(request,"login.html")