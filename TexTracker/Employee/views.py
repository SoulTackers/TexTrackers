 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import EmployeeForm,EmployeePostForm, AdminEmployeeAddForm
from .models import Employee, EmployeePost
from .forms import UserRegisterForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

def Employee_view(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST or None)
        form1 = EmployeePostForm(request.POST or None)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
    else:
        form = EmployeeForm(request.POST or None)
        form1 = EmployeePostForm(request.POST or None)
    context = {
        'form' : form,
        'form1' : form1
    }
    return render(request,'Employee/employee.html',context)

def AdminAddEmployeeView(request):
    if request.method == 'POST':
        form2 = EmployeeForm(request.POST)
        form3 = AdminEmployeeAddForm(request.POST)

        if form3.is_valid():
            new_user = form3.save()
            employee = form2.save(commit=False)
            if employee.user_id is None:
                employee.user_id = new_user.id
            employee.employee_name = new_user.username
            form2.save()
            return redirect('logout')

    else:
        form2 = EmployeeForm()
        form3 = AdminEmployeeAddForm()
    return render(request, 'Employee/add-employee-admin.html', {'form3': form3['username']})

def UpdateEmployeeView(request, id=1):
    employee = get_object_or_404(Employee, employee_id=id)
    employee_update_form = EmployeeForm(request.POST or None, instance=employee)

    if employee_update_form.is_valid():
        employee_update_form.save()
        return redirect("logout")
    return render(request, 'Employee/update-employee.html', {'form': employee_update_form})

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
            return redirect('logout')
    else:
        form1 = UserRegisterForm()
        form2 = EmployeeForm()
    return render(request, 'Employee/add-employee.html', {'form1': form1, 'form2': form2})

def DeleteEmployeeView(request, id):
    try:
        user = Employee.objects.get(employee_id=id).user
        user.delete()
        return render(request, 'delete_success.html', {'object':'AccountType', 'name':name})
    except e:
        return render(request, 'delete_unsuccess.html', {'object':'AccountType', 'name':name})
