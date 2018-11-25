from django import forms
from .models import *
from django.contrib.auth.models import User

class Employee_login_form(forms.ModelForm):
    empid = forms.CharField(label='User ID')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Employee_details
        fields = ('empid','password')


class Employee_details_form(forms.ModelForm):
    #BirthDate = forms.DateField(label ='BirthDate', widget = forms.SelectDateWidget(years=range(1990,2100)))
    #Dateofjoining = forms.DateField(label='Date of Joining',widget=forms.SelectDateWidget(years=range(1990,2100)))
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Employee_details
        fields = ('empid', 'firstName', 'MiddleName', 'LastName','Address','Designation','password')


class e_task_form(forms.ModelForm):
    Start_date = forms.DateField(label='Start Date',widget=forms.SelectDateWidget(years=range(1920,2100)))
    End_Date = forms.DateField(label='End Date',widget=forms.SelectDateWidget(years=range(1920,2100)))
    Emp = forms.CharField(initial='Not required ')

    class Meta:
        model = Task
        fields=('Task_description','Emp','Start_date','End_Date')