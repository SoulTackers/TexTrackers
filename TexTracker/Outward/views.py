# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import OutwardForm
from django.shortcuts import render,get_object_or_404,render_to_response
from .models import Outward




def outward_view(request):
    if request.method == 'POST':
        form = OutwardForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = OutwardForm(request.POST or None)
        print(Outward.objects.all())
    context = {
        'form' : form
    }
    return render(request,'Outward/outward.html',context)

def outward_update(request,id):
    outward = get_object_or_404(Outward,outward_id=id)
    outward_update_form = OutwardForm(request.POST or None,instance=outward)

    if outward_update_form.is_valid():
        outward_update_form.save()
    
    return render(request,'Outward/outward.html',{'form':outward_update_form})
