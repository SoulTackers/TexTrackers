 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import EmployeeForm,EmployeePostForm
from .models import Employee
from .forms import UserRegisterForm
from django.shortcuts import render, redirect, get_object_or_404
# from .helper import crispy_helper

# Create your views here.

def Employee_view(request):
    form = EmployeeForm(request.POST or None)
    form1 = EmployeePostForm(request.POST or None)
    if form.is_valid() and form1.is_valid():
        form.save()
        form1.save()
    context = {
        'form' : form,
        'form1' : form1
    }
    return render(request,'Employee/employee.html',context)

def AddEmployeeView(request):
    if request.method == 'POST':
        form1 = UserRegisterForm(request.POST)
        form2 = EmployeeForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            new_user = form1.save()
            employee = form2.save(commit=False)
            if employee.user_id is None:
                employee.user_id = new_user.id
            form2.save()
    else:
        form1 = UserRegisterForm()
        form2 = EmployeeForm()
    return render(request, 'Employee/add-employee.html', {'form1': form1, 'form2': form2})

def UpdateEmployeeView(request, id=1):
    employee = get_object_or_404(Employee, employee_id = id)
    employee_update_form = EmployeeForm(request.POST or None, instance=employee)

    if employee_update_form.is_valid():
        employee_update_form.save()
        return redirect("logout")
    return render(request, 'Employee/update-employee.html', {'employee_update_form': employee_update_form})
