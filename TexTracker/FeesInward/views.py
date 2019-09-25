# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import FeesinwardForm
from django.shortcuts import render,get_object_or_404,render_to_response
from django.shortcuts import render
from .models import Feesinward

# Create your views here.
def feesinward_view(request):
    if request.method == 'POST':
        form = FeesinwardForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = FeesinwardForm(request.POST or None)
    
    context = {
        'form' : form
    }
    return render(request,'FeesInward/feesinward.html',context)

def feesinward_update_view(request,id):
    feesinward = get_object_or_404(Feesinward,outward_id=id)
    feesinward_update_form = FeesinwardForm(request.POST or None,instance=feesinward)

    if feesinward_update_form.is_valid():
        feesinward_update_form.save()
    
    return render(request,'FeesInward/feesinward.html',{'form':feesinward_update_form})