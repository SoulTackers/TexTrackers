# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import PendingWorkForm
from django.shortcuts import render

# Create your views here.
def PendingWork_view(request):
    form = PendingWorkForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request,'PendingWork/pendingwork.html',context)