# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import InwardForm
from django.shortcuts import render

# Create your views here.
def Inward_view(request):
    form = InwardForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request,'Inward/inward.html',context)