from django.db import models


class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=10)
    student_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    grade = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)


class Payment(models.Model):
    id = models.BigAutoField(primary_key=True)
    payment_status = models.BooleanField(default=False)
    payment_type = models.CharField(
        max_length=20,
        choices=[("Registeration", "registration"), ("Penalty", "penalty")],
    )

    amount = models.FloatField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255)