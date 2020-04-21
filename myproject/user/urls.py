# from django.urls import path,include
# from rest_framework import routers
# from .views import retrieve1

# #Create your url patters here

from django.conf.urls import url, include
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
	path('register',views.register ,name='register'),
	
	# path('login',views.login ,name='login')


]


