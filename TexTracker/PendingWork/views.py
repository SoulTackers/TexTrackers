# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import PendingWorkForm
from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,render_to_response
from .models import PendingWork
from Inward.models import Inward
# Create your views here.
def pendingwork_view(request):
    if request.method == 'POST':
        form = PendingWorkForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = PendingWorkForm()
    context = {
        'form' : form
    }
    return render(request,'PendingWork/pendingwork.html',context)

def pendingwork_update_view(request,id):
    pendingwork = get_object_or_404(PendingWork,PendingWork_postid=id)
    pendingwork_update_form = PendingWorkForm(request.POST or None,instance=pendingwork)

    if pendingwork_update_form.is_valid():
        pendingwork_update_form.save()
    
    return render(request,'PendingWork/pendingwork.html',{'form':pendingwork_update_form})


def dashboard(request):
    pendingwork = PendingWork.objects.filter(PendingWork_employeeid = request.user.id)
    inwardlist = []
    i=5
    for pw in pendingwork:
        inward = Inward.objects.get(inward_id = pw.PendingWork_inwardid)
        inwardlist.append(inward)
    

    return render(request,'PendingWork/dashboard.html',{'work_list': pendingwork,'inwards':inwardlist,'i':i})