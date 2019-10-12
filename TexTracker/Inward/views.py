# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import InwardForm,InwardPostTypeForm,InwardTypesForm,InwardDocumentForm,InwardPendingDocumentForm
from PendingWork.forms import PendingWorkForm
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .models import Inward,InwardTypes,InwardPostType,InwardDocument,InwardPendingDocument
from Outward.forms import OutwardForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
@login_required(login_url='login')
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
            form = InwardForm()
            if inward_created :
                subject = 'Work On Your Application has been started..'
                message = ' It Will be Completed soon '
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['meetsuthar64@gmail.com'] #inwardform.inward_client_id.client_email
                send_mail( subject, message, email_from, recipient_list,fail_silently=False)

        if inwardDocumentForm.is_valid():
            documentform = inwardDocumentForm.save(commit=False)
            if documentform.inward_doc == None:
                temp = inwardPendingDocumentForm.save(commit=False)
                temp.inward = new_inward
                #temp.save()
            else:
                documentform.save()
            inwardDocumentForm = InwardDocumentForm()
            messages.add_message(request, messages.SUCCESS, 'Inward successfuly added with documents')
        else:
            InwardPendingDocumentForm.inward = new_inward
            messages.warning(request, 'Document is not valid')
    else:
        inwardform = InwardForm()
        # inwardposttypeform = InwardPostTypeForm(request.POST or None)
        # inwardtypesform = InwardTypesForm(request.POST or None)
        inwardDocumentForm = InwardDocumentForm()
        messages.add_message(request, messages.ERROR, 'Inward not added')
    context = {
        'form' : inwardform,
        # 'ipt_form' : inwardposttypeform,
        # 'it_form' : inwardtypesform,
        'image_form' : inwardDocumentForm,
    }
    return render(request,'Inward/inward.html',context)

@login_required(login_url='login')
def Inward_update_view(request, id):
    inward = get_object_or_404(Inward,inward_id=id)
    inward_image = get_object_or_404(InwardDocument,inward_id=id)

    if request.method == 'POST':
        inwardform = InwardForm(request.POST or None,instance=inward)
        inwardDocumentForm = InwardDocumentForm(request.POST or None,instance=inward_image)

        if inwardform.is_valid():
            inwardform.save()
            if inwardDocumentForm.is_valid():
                inwardDocumentForm.save()
                messages.add_message(request, messages.SUCCESS, 'Inward Successfully updated with documents')
                return redirect('list-inward')
            else:
                InwardPendingDocumentForm.inward = inwardform
                messages.warning(request, 'Document is not valid')
                return redirect('list-inward')

    else:
        inwardform = InwardForm(request.POST or None,instance=inward)
        inwardDocumentForm = InwardDocumentForm(request.POST or None,instance=inward_image)
    context = {
        'form' : inwardform,
        'image_form' : inwardDocumentForm,
    }
    return render(request,'Inward/inward.html',context)

@login_required(login_url='login')
def DeleteInwardView(request, id):
    try:
        obj = Inward.objects.get(account_type_id=id)
        name = str(obj)
        obj.delete()
        return render(request, 'delete_success.html', {'object':'Inward', 'name':name})
    except:
        return render(request, 'delete_success.html', {'object':'e', 'name':'error'})


@login_required(login_url='login')
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

@login_required(login_url='login')
def AddInwardTypesView(request):
    if request.method == 'POST':
        inwardTypesForm = InwardTypesForm(request.POST or None)
        if inwardTypesForm.is_valid():
            inwardTypesForm.save()
        return redirect('added')
    else:
        inwardTypesForm = InwardTypesForm(request.POST or None)
        return render(request, 'Client/add-service.html', {'form': inwardTypesForm})

@login_required(login_url='login')
def UpdateInwardTypesView(request, id):
    service = get_object_or_404(InwardTypes, pk=id)
    inwardTypesForm = InwardTypesForm(request.POST or None, instance=service)
    if inwardTypesForm.is_valid():
        inwardTypesForm.save()
    return render(request, 'Client/add-service.html', {'form': inwardTypesForm})

@login_required(login_url='login')
def DeleteInwardTypesView(request, id):
    try:
        obj = InwardTypes.objects.get(account_type_id=id)
        name = str(obj)
        obj.delete()
        return render(request, 'delete_success.html', {'object':'InwardTypes', 'name':name})
    except:
        return render(request, 'delete_success.html', {'object':'e', 'name':'error'})


# inward post types views.........................................................................

@login_required(login_url='login')
def AddInwardPostTypesView(request):
    if request.method == 'POST':
        inwardPostTypesForm = InwardPostTypesForm(request.POST or None)
        if inwardPostTypesForm.is_valid():
            inwardPostTypesForm.save()
        return redirect('added')
    else:
        inwardPostTypesForm = InwardPostTypesForm(request.POST or None)
        return render(request, 'Client/add-service.html', {'form': inwardPostTypesForm})

@login_required(login_url='login')
def UpdateInwardPostTypesView(request, id):
    service = get_object_or_404(InwardPostTypes, pk=id)
    inwardPostTypesForm = InwardPostTypesForm(request.POST or None, instance=service)
    if inwardPostTypesForm.is_valid():
        inwardPostTypesForm.save()
    return render(request, 'Client/add-service.html', {'form': inwardPostTypesForm})

@login_required(login_url='login')
def DeleteInwardPostTypesView(request, id):
    try:
        obj = InwardPostTypes.objects.get(account_type_id=id)
        name = str(obj)
        obj.delete()
        return render(request, 'delete_success.html', {'object':'InwardPostTypes', 'name':name})
    except:
        return render(request, 'delete_success.html', {'object':'e', 'name':'error'})


@login_required(login_url='login')
def inward_list_view(request):
    inwards = Inward.objects.all()
    return render(request,'Inward/inward_list.html',{'inwards':inwards})

def AdddocumentView(request):
    if request.method == 'POST':
        p_form = InwardDocumentForm(request.POST, request.FILES)
        if p_form.is_valid():
            p_form.save()
            messages.success(
                request, f'Your account has been Updated!')
            return HttpResponse("Done!")
    else:
        p_form = InwardDocumentForm(request.POST, request.FILES)

    context = {
        'form': p_form,
    }

    return render(request, 'Inward/addfile.html', context)
