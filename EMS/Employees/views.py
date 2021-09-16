from django.shortcuts import render
from rest_framework.response import Response
from .models import Employees
from .serializer import   EmployeesSerializer
from rest_framework.views import APIView 



# Create your views here.
class EmployeeList(APIView):
    
    def get(self,request, format = None):
        employee = Employees.objects.all()
        serialize_class = EmployeesSerializer(employee, many= True)
        return Response(serialize_class.data)
        