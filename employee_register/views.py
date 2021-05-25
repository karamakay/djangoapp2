from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

import datetime
from django.db.models import Count


from datetime import date, timedelta

import django_filters
# Create your views here.

def returnA():

    '''
    for i in Employee.objects.values('operation').annotate(c=Count('operation')).order_by('-c'):
        print(i["operation"],i["c"])
    '''


    for i in Employee.objects.values('operation').annotate(c=Count('operation')).order_by('-c'):
        if(i["operation"]==1):
            Employee.objects.filter(operation=1).update(frequency=int(i["c"])/Employee.objects.latest('id').id)
        elif(i["operation"]==2):
            Employee.objects.filter(operation=2).update(frequency=int(i["c"])/Employee.objects.latest('id').id)
        elif(i["operation"]==3):
            Employee.objects.filter(operation=3).update(frequency=int(i["c"])/Employee.objects.latest('id').id)
        elif(i["operation"]==4):
            Employee.objects.filter(operation=4).update(frequency=int(i["c"])/Employee.objects.latest('id').id)

        print(i)

    print(Employee.objects.values('operation').annotate(c=Count('operation')).order_by('-c')[1]["c"])


    print(Employee.objects.filter(datetimeC__gt=(date.today() - timedelta(days=2)), datetimeC__lte= datetime.datetime.now()).all())
    return Employee.objects.filter(datetimeC__gt=(date.today() - timedelta(days=2)), datetimeC__lte= datetime.datetime.now()).all()

#Employee.objects.all()

def employee_list(request):
    context = {'employee_list':returnA() }
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
