from django.contrib import admin
from django.urls import path,include
from drapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('team/',views.team),
    path('service/',views.service),
    path('appointment/',views.appointment),
    path('testimonial/',views.testimonial),
    path('feature/',views.feature),
]
