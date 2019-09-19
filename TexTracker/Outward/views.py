# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import OutwardForm
from django.shortcuts import render

# Create your views here.
def Outward_view(request):
    form = OutwardForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request,'Outward/outward.html',context)