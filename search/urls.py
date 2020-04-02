# from django.urls import path,include
# from rest_framework import routers
# from .views import retrieve1

# #Create your url patters here
# urlpatterns = [
   

#      path('', retrieve1),
# ]
from django.conf.urls import url, include
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
	path('', views.home, name='home'),

    path('search/', views.SearchView.as_view(), name='search'),

]


