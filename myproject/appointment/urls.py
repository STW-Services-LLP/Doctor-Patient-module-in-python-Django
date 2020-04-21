from django.urls import path,include

from . import views

#urls for doctor related api's

urlpatterns = [
   
     path('appointment/', views.appointment , name= 'appointment'),
     path('appointment-request/', views.appointment_request),
     path('appointment-details/<int:id>/', views.appointment_details)
    
    
]
