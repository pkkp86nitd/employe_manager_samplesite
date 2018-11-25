from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from  .forms import *
from django.conf import settings
from .models import *
from django.contrib.auth.models import User



# authetication method for login to employee portal
def authenticate(a,b):
    form = Employee_details.objects.filter(empid= a,password = b).exists()
    return form

#login view
@csrf_exempt
def login(request):
    if request.method == "POST":
        form = Employee_login_form(data=request.POST)
        if form.is_valid():
            p = request.POST
            eid = p.get('empid',False)
            pd = p.get('password',False)
            a = authenticate(eid,pd)
            if a is True:
                request.session['emp'] = eid
                request.session['pwd']=pd
                return redirect('home')
            else:
                return HttpResponse('Error')
    else:
        form =Employee_login_form()
    return render(request, 'Employeemanager/login.html', {'form': form})

#Register new employee
@csrf_exempt
def register(request):
        if request.method == "POST":
            form = Employee_details_form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = Employee_details_form()
        return render(request, 'Employeemanager/RegisterEmployee.html', {'form': form})


#Home View
def home(request):
    empid = request.session['emp']
    pwd = request.session['pwd']
    if authenticate(empid,pwd) is True:
        request.session['empid'] = empid
        request.session['pwd'] = pwd
        Employee = Employee_details.objects.filter(empid = empid)
        return render(request,'Employeemanager/home.html',{'Employee':Employee})


#Logout View
#{'next_page': settings.LOGOUT_REDIRECT_URL}
def logout(request):
    request.session.flush()
    return render(request,'Employeemanager/logout.html',{'next_page': settings.LOGOUT_REDIRECT_URL})




#performance view
@csrf_exempt
def performance(request):
    empid = request.session['empid']
    Employee = Employee_details.objects.filter(empid=empid)
    if request.method == "POST":
        form = e_task_form(request.POST)
        if form.is_valid():
           obj = form.save(commit=True)
           obj.Emp = empid
           obj.save()
           return redirect('home')
    else:
         form = e_task_form()
         return render(request, 'Employeemanager/Add_Task.html', {'form': form ,'Employee':Employee})

def view_task_detail(request):
    empid = request.session['empid']
    Tasks  = Task.objects.filter(Emp = empid)
    Employee = Employee_details.objects.filter(empid=empid)
    return render(request,'Employeemanager/View_Tasks.html',{'Tasks':Tasks,'Employee':Employee})
