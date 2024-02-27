from django.shortcuts import render
from django.http import HttpResponse

from .models import Student


def fullStudents(request):
    students = Student.objects.values("student_name", "phone_number", "student_id")
    return render(request, "users/students.html", {"student_list": students})


def getStudentByID(request, student_id):
    try:
        context = {}
        student = Student.objects.get(student_id=student_id)
        context["student_list"] = [student]
        return render(request, "users/student.html", context)
    except:
        return HttpResponse(
            f"Error while getting a student with the id of {student_id}"
        )


def getStudentByName(request, student_name):
    context = {}
    try:
        student = Student.objects.filter(student_name__contains=student_name)
        context["student_list"] = student
        return render(request, "users/student.html", context)
    except:
        return HttpResponse(
            f"Error while getting a student with the name of {student_name}"
        )