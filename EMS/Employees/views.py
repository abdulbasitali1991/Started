import re
from django.http.response import Http404
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


class EmployeeDetail(APIView):
    def get_object(self,pk):
        try :
             return Employees.objects.get(pk = pk)
        except Employees.DoesNotExist :
            raise Http404
        
        
    def get(self,request,pk ,format =None):
        obj = self.get_object(pk)
        serialize_class = EmployeesSerializer(obj)
        return Response(serialize_class.data);
    
    
    def put(self,request,pk, format = None):
        obj = self.get_object(pk)
        serialize_class = EmployeesSerializer(obj,data=request.data)
        if serialize_class.is_valid():
            return Response("data Updated",status.HTTP_202_ACCEPTED)
        return Response("not accepted",status.HTTP_304_NOT_MODIFIED)
    
    def delete(self ,request,pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response("data deleted",status=status.HTTP_204_NO_CONTENT)
    



        