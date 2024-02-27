from django.db import models
from django.contrib.auth.models import AbstractUser, User

class UserExtend(AbstractUser):
    phoneNumber = models.CharField("Phone number", max_length=11, blank=False)
    ssn = models.CharField("National Code", max_length=10, blank=False)
    mobileStatus = models.BooleanField("Phone Verification", default=False, blank=False)
    emailStatus = models.BooleanField("Email Verification", default=False, blank=False)
    is_admin = models.BooleanField(default=False, blank=False)
    credit = models.DecimalField(
        "Credit", default=10000000, max_digits=10, decimal_places=0, blank=True
    )

    FILEDS_TO_UPDATE = ["email", "phoneNumber"]
    REQUIRED_FILEDS = ["email", "phoneNumber", "first_name", "last_name"]
