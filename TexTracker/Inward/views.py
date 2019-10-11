# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import InwardForm,InwardPostTypeForm,InwardTypesForm,InwardDocumentForm,InwardPendingDocumentForm
from PendingWork.forms import PendingWorkForm
from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from .models import Inward,InwardTypes,InwardPostType,InwardDocument,InwardPendingDocument
from PendingWork.models import PendingWork
from Outward.forms import OutwardForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponse


# Create your views here.
def handle_uploaded_file(f):
    with open('myapp/static/upload/'+'abc.c', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def Inward_view(request):
    if request.method == 'POST':
        inwardform = InwardForm(request.POST or None, request.FILES or None)
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
            """else:
                handle_uploaded_file(documentform.inward_doc)"""
            documentform.save()
            #messages.success(request, 'Document is valid')
        else:
            InwardPendingDocumentForm.inward = new_inward
            messages.warning(request, 'Document is not valid')
        return redirect('add-inward')

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


def Inward_update_view(request, id):
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


def DeleteInwardView(request, id):
    try:
        obj = Inward.objects.get(account_type_id=id)
        name = str(obj)
        obj.delete()
        return render(request, 'delete_success.html', {'object':'Inward', 'name':name})
    except:
        return render(request, 'delete_success.html', {'object':'e', 'name':'error'})


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


# inward types views.........................................................................

def AddInwardTypesView(request):
    if request.method == 'POST':
        inwardTypesForm = InwardTypesForm(request.POST or None)
        if inwardTypesForm.is_valid():
            inwardTypesForm.save()
        return redirect('added')
    else:
        inwardTypesForm = InwardTypesForm(request.POST or None)
        return render(request, 'Client/add-service.html', {'form': inwardTypesForm})


def UpdateInwardTypesView(request, id):
    service = get_object_or_404(InwardTypes, pk=id)
    inwardTypesForm = InwardTypesForm(request.POST or None, instance=service)
    if inwardTypesForm.is_valid():
        inwardTypesForm.save()
    return render(request, 'Client/add-service.html', {'form': inwardTypesForm})


def DeleteInwardTypesView(request, id):
    try:
        obj = InwardTypes.objects.get(account_type_id=id)
        name = str(obj)
        obj.delete()
        return render(request, 'delete_success.html', {'object':'InwardTypes', 'name':name})
    except:
        return render(request, 'delete_success.html', {'object':'e', 'name':'error'})


# inward post types views.........................................................................


def AddInwardPostTypesView(request):
    if request.method == 'POST':
        inwardPostTypesForm = InwardPostTypesForm(request.POST or None)
        if inwardPostTypesForm.is_valid():
            inwardPostTypesForm.save()
        return redirect('added')
    else:
        inwardPostTypesForm = InwardPostTypesForm(request.POST or None)
        return render(request, 'Client/add-service.html', {'form': inwardPostTypesForm})


def UpdateInwardPostTypesView(request, id):
    service = get_object_or_404(InwardPostTypes, pk=id)
    inwardPostTypesForm = InwardPostTypesForm(request.POST or None, instance=service)
    if inwardPostTypesForm.is_valid():
        inwardPostTypesForm.save()
    return render(request, 'Client/add-service.html', {'form': inwardPostTypesForm})


def DeleteInwardPostTypesView(request, id):
    try:
        obj = InwardPostTypes.objects.get(account_type_id=id)
        name = str(obj)
        obj.delete()
        return render(request, 'delete_success.html', {'object':'InwardPostTypes', 'name':name})
    except:
        return render(request, 'delete_success.html', {'object':'e', 'name':'error'})

#..................................................................................................................

def AdddocumentView(request):
    if request.method == 'POST':
        docupload = InwardDocumentForm(request.POST, request.FILES)
        #doc = docupload.save(commit=False)
        print(request.POST)
        # if post.inward_doc == None:
            #return HttpResponse("File not found")
        if docupload.is_valid():
            #handle_uploaded_file(request.POST['inward_doc']) # request.FILES['inward_doc'])
            docupload.save()
            return HttpResponse("File uploaded successfuly")
        #return redirect('added')
    else:
        docupload = InwardDocumentForm(request.POST or None)
        return render(request, 'Inward/addfile.html', {'form': docupload})
