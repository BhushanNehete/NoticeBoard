from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.


class Department(models.Model):
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.department


class Notice(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    notice_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


class ContactUs(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    Email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()
