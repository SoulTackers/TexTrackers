# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import InwardForm,InwardPostTypeForm,InwardTypesForm
from django.shortcuts import render

# Create your views here.
def Inward_view(request):
    inwardform = InwardForm(request.POST or None)
    inwardposttypeform = InwardPostTypeForm(request.POST or None)
    inwardtypesform = InwardTypesForm(request.POST or None)
    if inwardform.is_valid() and inwardposttypeform.is_valid() and inwardtypesform.is_valid():
        inwardform.save()
        inwardposttypeform.save()
        inwardtypesform.save()
    context = {
        'form' : inwardform,
        'ipt_form' : inwardposttypeform,
        'it_form' : inwardtypesform
    }
    return render(request,'Inward/inward.html',context)