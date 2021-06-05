from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    phone_no  = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=200, default="")