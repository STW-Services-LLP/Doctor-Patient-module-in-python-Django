from django.contrib.auth import authenticate, login, logout   
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django import forms
from django.utils.translation import gettext as _
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
CustomUser = get_user_model()
class RegisterForm(UserCreationForm):
	email = forms.EmailField()
	
	# first_name = forms.CharField()
	# last_name = forms.CharField()

	class Meta:
		model = CustomUser
		fields = ['username','email','password1','password2' ,'is_patient','is_doctor']
# class LoginForm(AuthenticationForm):

# 	class Meta:
# 		model = CustomUser
# 		fields = ['username','password']