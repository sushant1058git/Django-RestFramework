from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
from .serializers import EmployeeSerializers


def employeeListView(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializers(employees, many=True)
    return JsonResponse(serializer.data, safe=False)
