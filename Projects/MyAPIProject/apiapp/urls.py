from django.contrib import admin
from django.urls import path,include
from apiapp import views

urlpatterns = [
    path('getall/',views.getall),
    path('getstid/<int:id>',views.getstid),
    path('deletestid/<int:id>',views.deletestid),
    path('savedata/',views.savedata),
]