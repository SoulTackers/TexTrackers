# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import EmployeeForm

from django.shortcuts import render

# Create your views here.

def Employee_view(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request,'Employee/employee.html',context)
