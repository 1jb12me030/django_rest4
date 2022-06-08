from django.shortcuts import render
from testapp.models import Employee

from rest_framework.viewsets import ModelViewSet
from testapp.serializers import EmployeeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class Employee(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
