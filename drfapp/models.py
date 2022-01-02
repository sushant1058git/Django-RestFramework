from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
