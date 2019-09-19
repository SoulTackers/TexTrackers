# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import FeesinwardForm
from django.shortcuts import render

# Create your views here.
def Feesinward_view(request):
    form = FeesinwardForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request,'FeesInward/feesinward.html',context)