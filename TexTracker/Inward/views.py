# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import InwardForm,InwardPostTypeForm,InwardTypesForm,InwardImageForm
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def Inward_view(request):
    inwardform = InwardForm(request.POST or None)
    inwardposttypeform = InwardPostTypeForm(request.POST or None)
    inwardtypesform = InwardTypesForm(request.POST or None)
    inwardimageform = InwardImageForm(request.POST or None)
    if inwardform.is_valid() and inwardposttypeform.is_valid() and inwardtypesform.is_valid():
        inwardform.save()
        inwardposttypeform.save()
        inwardtypesform.save()
    if inwardimageform.is_valid():
        inwardimageform.save()
        messages.success(request, 'image is valid')
    else:
        messages.warning(request, 'image is not valid')

    context = {
        'form' : inwardform,
        'ipt_form' : inwardposttypeform,
        'it_form' : inwardtypesform,
        'image_form' : inwardimageform,
    }
    return render(request,'Inward/inward.html',context)
