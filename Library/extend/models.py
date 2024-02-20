from django.db import models
from django.contrib.auth.models import AbstractUser

class UserExtend(AbstractUser):
    Payment_ID = models.IntegerField(primary_key=True)
    Mobile_Text = models.CharField(max_length=255)
    Payment_Status = models.BooleanField(default=False)
    Payment_Date = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    Payment_Type = models.CharField(max_length=255)
    Mobile_Status = models.BooleanField(default=False)
    IsAdmin = models.BooleanField(default=False)
    Email_Status = models.BooleanField(default=False)
    Credit = models.FloatField(default=0.0)
    National_Text = models.CharField(max_length=255)
    Student_ID = models.CharField(max_length=255)

    def __str__(self):
        return str(self.Payment_ID)
