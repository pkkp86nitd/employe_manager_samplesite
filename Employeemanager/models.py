from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.
class Employee_details(models.Model):
    empid = models.CharField(max_length=10)
    firstName = models.CharField(max_length=20)
    MiddleName = models.CharField(max_length=20,blank=True)
    LastName = models.CharField(max_length= 20)
    Address = models.TextField()
    Designation = models.CharField(max_length=20)
    password = models.CharField(max_length = 10)
    addedBy = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return str(self.empid)


class Task(models.Model):
    Task_id = models.AutoField(primary_key=True)
    Emp = models.CharField(max_length=10)
    Task_description = models.TextField(max_length = 200)
    Start_date = models.DateField()
    End_Date = models.DateField()

    def __str__(self):
        return str(self.Task_id)