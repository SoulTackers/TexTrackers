# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import InwardForm,InwardPostTypeForm,InwardTypesForm,InwardDocumentForm,InwardPendingDocumentForm
from PendingWork.forms import PendingWorkForm
from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from .models import Inward,InwardTypes,InwardPostType,InwardDocument,InwardPendingDocument
from Outward.forms import OutwardForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
# Create your views here.
def Inward_view(request):
    if request.method == 'POST':
        inwardform = InwardForm(request.POST or None)
        # inwardposttypeform = InwardPostTypeForm(request.POST or None)
        # inwardtypesform = InwardTypesForm(request.POST or None)
        inwardDocumentForm = InwardDocumentForm(request.POST or None)
        inwardPendingDocumentForm = InwardPendingDocumentForm(request.POST or None)

        if inwardform.is_valid():
            form = InwardForm(request.POST)
            new_inward = form.save(commit=False)
            new_inward.inward_track = str(request.user.id) + ": Created,"
            inward_created = new_inward.save()
            print(new_inward)
            if inward_created :
                subject = 'Work On Your Application has been started..'
                message = ' It Will be Completed soon '
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['',] #inwardform.inward_client_id.client_email
                send_mail( subject, message, email_from, recipient_list,fail_silently=False)

        if inwardDocumentForm.is_valid():
            documentform = inwardDocumentForm.save(commit=False)
            if documentform.inward_doc == None:
                temp = inwardPendingDocumentForm.save(commit=False)
                temp.inward = new_inward
                temp.save()
            documentform.save()
            #messages.success(request, 'Document is valid')
        else:
            InwardPendingDocumentForm.inward = new_inward
            messages.warning(request, 'Document is not valid')            
    else:
        inwardform = InwardForm(request.POST or None)
        # inwardposttypeform = InwardPostTypeForm(request.POST or None)
        # inwardtypesform = InwardTypesForm(request.POST or None)
        inwardDocumentForm = InwardDocumentForm(request.POST or None)
    context = {
        'form' : inwardform,
        # 'ipt_form' : inwardposttypeform,
        # 'it_form' : inwardtypesform,
        'image_form' : inwardDocumentForm,
    }
    return render(request,'Inward/inward.html',context)


def Inward_update_view(request):
    inward = get_object_or_404(Inward,inward_id=id)
    inward_image = get_object_or_404(InwardDocument,inward_id=id)
    inwardform = InwardForm(request.POST or None,instance=inward)
    inwardDocumentForm = InwardDocumentForm(request.POST or None,instance=inward_image)

    if inwardform.is_valid():
        inwardform.save()
        if inwardDocumentForm.is_valid():
            inwardDocumentForm.save()
            #messages.success(request, 'Document is valid')
        else:
            InwardPendingDocumentForm.inward = inwardform
            messages.warning(request, 'Document is not valid')
    context = {
        'form' : inwardform,
        'image_form' : inwardDocumentForm,
    }
    return render(request,'Inward/inward.html',context)



def inward_pass(request,id):
    if request.method == 'POST':
        inward = Inward.objects.get(inward_no = request.POST['inwardno'])
        inward.inward_employeeid = request.POST['empid']
        inward.inward_track = inward.inward_track + str(request.user.id)+": "+request.POST['workdone']
        inward.save()

        # Begin Mail..............
        subject = 'Work Progress'
        message = request.POST['workdone']+'Done by '+inward.inward_employeeid.employee_name
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['',] #inwardform.inward_client_id.client_email
        send_mail( subject, message, email_from, recipient_list,fail_silently=False)
        # End Mail.................

    inward = get_object_or_404(Inward,inward_id=id)
    outward = OutwardForm(request.POST or None)
    outward.fields['outward_iid'].initial = inward

    context = {
        'inward':inward,
        'outward':outward
    }    
    return render(request,'Inward/passinward.html',context)

