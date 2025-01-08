from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('',views.index),
   path('signup/',views.signup,name='signup'),
   path('notes/',views.notes,name='notes'),
   path('profile/',views.profile,name='profile'),
   path('about/',views.about,name='about'),
   path('contact/',views.contact,name='contact'),
   path('userlogout/',views.userlogout),
]
