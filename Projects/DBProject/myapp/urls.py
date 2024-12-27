from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('',views.index),
   path('showdata/',views.showdata,name='showdata'),
   path('updatedata/<int:id>',views.updatedata),
   path('deletedata/<int:id>',views.deletedata),
]