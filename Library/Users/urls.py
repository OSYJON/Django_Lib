from django.contrib import admin
from django.urls import path, include
from Users import views

urlpatterns = [
    path("students/", views.fullStudents, name="list"),
    path("students/id/<int:student_id>", views.getStudentByID),
    path("students/name/<str:student_name>", views.getStudentByName),
]
