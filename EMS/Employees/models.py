from django.db import models
from django.db.models.fields import BigIntegerField, IntegerField

# Create your models here.
class Employees(models.Model):
    Id = IntegerField(primary_key=True)
    First_Name = models.CharField(max_length=221)
    Last_Name = models.CharField(max_length=224)
    Department = models.CharField(max_length=225)
    Experience = models.IntegerField()
    Salary = BigIntegerField()
    Date_OF_Joinig = models.DateField()
    