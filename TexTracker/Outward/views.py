# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import OutwardForm
from django.shortcuts import render,get_object_or_404,render_to_response
from .models import Outward
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login')
def outward_view(request):
    if request.method == 'POST':
        form = OutwardForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Outward is added')
            form = OutwardForm()
            # Begin Mail..............
            subject = 'Work On Your Application has been started..'
            message = ' It Will be Completed soon '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['',] #inwardform.inward_client_id.client_email
            send_mail( subject, message, email_from, recipient_list,fail_silently=False)
            # End Mail.................
    else:
        form = OutwardForm()
        print(Outward.objects.all())
    context = {
        'form' : form
    }
    return render(request,'Outward/outward.html',context)

@login_required(login_url='login')
def outward_update(request,id):
    outward = get_object_or_404(Outward,outward_id=id)
    outward_update_form = OutwardForm(request.POST or None,instance=outward)

    if outward_update_form.is_valid():
        outward_update_form.save()
        messages.add_message(request, messages.SUCCESS, 'Outward Updated')

    return render(request,'Outward/outward.html',{'form':outward_update_form})

@login_required(login_url='login')
def DeleteOutwardView(request, id):
    try:
        obj = OutwardTypes.objects.get(account_type_id=id)
        name = str(obj)
        obj.delete()
        return render(request, 'delete_success.html', {'object':'OutwardTypes', 'name':name})
    except:
        return render(request, 'delete_success.html', {'object':'e', 'name':'error'})


@login_required(login_url='login')
def outward_list_view(request):
    outwards = Outward.objects.all()
    return render(request,'Outward/outward_list.html',{'outwards':outwards})