from django.contrib import admin
from django.urls import path, include
from Book import views

urlpatterns = [
    path("", views.fullBook, name="list"),
    path("id/<int:book_id>", views.getBookByID),
    path("name/<str:book_name>", views.getBookByName),
]