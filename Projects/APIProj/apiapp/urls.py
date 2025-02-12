from django.contrib import admin
from django.urls import path
from apiapp import views


urlpatterns = [
    path("", views.index),
    path("getall/", views.getall),
    path("getid/<int:id>", views.getid),
    path("deleteid/<int:id>", views.deleteid),
    path("insertdata/", views.insertdata),
    path("updatedata/<int:id>", views.updatedata),
]
