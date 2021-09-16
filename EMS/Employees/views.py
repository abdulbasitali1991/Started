from django.shortcuts import render
from rest_framework.response import Response
from .models import Employees
from .serializer import   EmployeesSerializer
from rest_framework.views import APIView 
from rest_framework import status



# Create your views here.
class EmployeeList(APIView):
    
    def get(self,request, format = None):
        employee = Employees.objects.all()
        serialize_class = EmployeesSerializer(employee, many= True)
        return Response(serialize_class.data)
    
    def post(self,request, format = None):
        serialize_class = EmployeesSerializer(data=request.data)
        if serialize_class.is_valid():
            serialize_class.save()
            return Response(serialize_class.data,status.HTTP_201_CREATED)
        return Response("data not added",status.HTTP_400_BAD_REQUEST)
        