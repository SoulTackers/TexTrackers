# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import InwardForm,InwardPostTypeForm,InwardTypesForm,InwardDocumentForm
from PendingWork.forms import PendingWorkForm
from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from .models import Inward,InwardTypes,InwardPostType,InwardDocument

# Create your views here.
def Inward_view(request):
    if request.method == 'POST':
        inwardform = InwardForm(request.POST or None)
        # inwardposttypeform = InwardPostTypeForm(request.POST or None)
        # inwardtypesform = InwardTypesForm(request.POST or None)
        inwardimageform = InwardDocumentForm(request.POST or None)
        
        if inwardform.is_valid():
            form = InwardForm(request.POST)
            new_inward = form.save(commit=False)
            new_inward.inward_track = str(request.user.id) + ": Created,"
            new_inward.save()
        if inwardimageform.is_valid():
            inwardimageform.save()
            messages.success(request, 'image is valid')
        else:
            messages.warning(request, 'image is not valid')
    else:
        inwardform = InwardForm(request.POST or None)
        # inwardposttypeform = InwardPostTypeForm(request.POST or None)
        # inwardtypesform = InwardTypesForm(request.POST or None)
        inwardimageform = InwardDocumentForm(request.POST or None)
    context = {
        'form' : inwardform,
        # 'ipt_form' : inwardposttypeform,
        # 'it_form' : inwardtypesform,
        'image_form' : inwardimageform,
    }
    return render(request,'Inward/inward.html',context)

def Inward_update_view(request):
    inward = get_object_or_404(Inward,inward_id=id)
    inward_image = get_object_or_404(InwardDocument,inward_id=id)
    inwardform = InwardForm(request.POST or None,instance=inward)
    inwardimageform = InwardDocumentForm(request.POST or None,instance=inward_image)
     
    if inwardform.is_valid():
        inwardform.save()
        if inwardimageform.is_valid():
            inwardimageform.save()
            messages.success(request, 'image is valid')
        else:
            messages.warning(request, 'image is not valid')
    context = {
        'form' : inwardform,
        'image_form' : inwardimageform,
    }
    return render(request,'Inward/inward.html',context)


def inward_pass(request):
    if request.method == 'POST':
        inward = Inward.objects.get(inward_no = request.POST['inwardno'])
        inward.inward_employeeid = request.POST['empid']
        inward.inward_track = inward.inward_track + str(request.user.id)+": "+request.POST['workdone']
        inward.save()
    return render(request,'Inward/passinward.html')