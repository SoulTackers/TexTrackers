# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import PendingWorkForm
from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,render_to_response
from .models import PendingWork
from Inward.models import Inward
from Client.models import Client
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
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

@login_required
def pendingwork_update_view(request,id):
    pendingwork = get_object_or_404(PendingWork,PendingWork_postid=id)
    pendingwork_update_form = PendingWorkForm(request.POST or None,instance=pendingwork)

    if pendingwork_update_form.is_valid():
        pendingwork_update_form.save()

    return render(request,'PendingWork/pendingwork.html',{'form':pendingwork_update_form})

@login_required
def dashboard(request):
    pendingwork = PendingWork.objects.all()
    inwardlist = []
    # clientlist = []
    print('Hello')
    for pw in pendingwork:
        inward = Inward.objects.get(inward_id = pw.PendingWork_inwardid.inward_id)
        #client = Client.objects.get(client_id = inward.inward_client_id.client_id)
        inwardlist.append(inward)
        #clientlist.append(client)
    # mydata = zip(inwardlist,clientlist)
    context = {
        'inwards':inwardlist,
        #'inward': inward,
        #'client': client,
    }


    return render(request,'PendingWork/dashboard.html',context)
