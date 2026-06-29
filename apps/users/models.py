from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.username




# from django.contrib.auth.models import AbstractUser:AbstractUser is Django's built-in user blueprint.
# Default Django User without creating a database table.It already contains everything needed for authentication.