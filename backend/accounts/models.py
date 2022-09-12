from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from transport.models import Stoppage

class User(AbstractUser):
    usertype = models.CharField(max_length=50, default='user')

    def __str__(self):
        return self.username

class Official(models.Model):
    official = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    contact_number = models.CharField(max_length=100)

    def __str__(self):
        return self.official.username

class Student(models.Model):
    student = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    contact_number = models.CharField(max_length=100)
    batch_number = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    stoppage = models.CharField(max_length=100, default='')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.student.username

class Teacher(models.Model):
    teacher = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
    contact_number = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    codename = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    stoppage = models.CharField(max_length=100, default='')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.teacher.username

class Staff(models.Model):
    staff = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    stoppage = models.CharField(max_length=100, default='')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.staff.username

def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)