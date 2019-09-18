# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import EmployeeForm,EmployeePostForm

from django.shortcuts import render

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
