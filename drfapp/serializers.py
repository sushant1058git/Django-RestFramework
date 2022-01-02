from django.db import models
from django.db.models import fields
from .models import Employee
from rest_framework import serializers


class EmployeeSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=30)
    password = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=10)
