 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import EmployeeForm,EmployeePostForm, AdminEmployeeAddForm
from .models import Employee, EmployeePost
from .forms import UserRegisterForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def Employee_view(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST or None)
        # form1 = EmployeePostForm(request.POST or None)
        if form.is_valid() :  #and form1.is_valid()
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Employee is added')
            form = EmployeeForm()
            # form1.save()
    else:
        form = EmployeeForm()
        # form1 = EmployeePostForm(request.POST or None)
    context = {
        'form' : form,
        # 'form1' : form1
    }
    return render(request,'Employee/employee.html',context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def UpdateEmployeeView(request):
    employee = get_object_or_404(Employee, employee_id=request.user.id)
    employee_update_form = EmployeeForm(request.POST or None, instance=employee)

    if employee_update_form.is_valid():
        employee_update_form.save()
        messages.add_message(request, messages.SUCCESS, 'Employee Profile is updated')
        return redirect("dashboard")
    return render(request, 'Employee/update-employee.html', {'form': employee_update_form})

@login_required(login_url='login')
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



@login_required(login_url='login')
def DeleteEmployeeView(request, id):
    try:
        emp = Employee.objects.get(employee_id=id)
        user = emp.user
        name = str(emp)
        user.delete()
        return render(request, 'delete_success.html', {'object':'Employee', 'name':name})
    except e:
        return render(request, 'delete_unsuccess.html', {'object':'Employee', 'name':'Employee not found'})


# Employee Post Views..........................................................................................

@login_required(login_url='login')
def AddEmployeePostView(request):
    if request.method == 'POST':
        employeePostForm = EmployeePostForm(request.POST or None)
        if employeePostForm.is_valid():
            employeePostForm.save()
        return redirect('added')
    else:
        employeePostForm = EmployeePostForm(request.POST or None)
        return render(request, 'Client/add-service.html', {'form': employeePostForm})

@login_required(login_url='login')
def UpdateEmployeePostView(request, id):
    service = get_object_or_404(EmployeePost, pk=id)
    employeePostForm = EmployeePostForm(request.POST or None, instance=service)
    if employeePostForm.is_valid():
        employeePostForm.save()
    return render(request, 'Client/add-service.html', {'form': employeePostForm})

@login_required(login_url='login')
def DeleteEmployeePostView(request, id):
    try:
        obj = EmployeePost.objects.get(account_type_id=id)
        name = str(obj)
        obj.delete()
        return render(request, 'delete_success.html', {'object':'EmployeePost', 'name':name})
    except:
        return render(request, 'delete_success.html', {'object':'e', 'name':'error'}) 
