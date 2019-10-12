# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404,render_to_response
from .forms import InvoiceForm,ServicetypeForm
from django.shortcuts import render
from .models import Invoice,Servicetype
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def invoice_view(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Invoice is added')
            form = InvoiceForm()
    else:
        form = InvoiceForm()
        messages.add_message(request, messages.ERROR, 'Invoice is not added')
    context = {
        'form' : form,
    }
    return render(request,'Invoice/invoice.html',context)

@login_required(login_url='login')
def invoice_update_view(request,id):
    invoice = get_object_or_404(Invoice,invoice_id=id)
    invoice_update_form = InvoiceForm(request.POST or None,instance=invoice)

    if invoice_update_form.is_valid():
        invoice_update_form.save()
        messages.add_message(request, messages.SUCCESS, 'Invoice is updated')

    return render(request,'Invoice/invoice.html',{'form':invoice_update_form})

@login_required(login_url='login')
def DeleteInvoiceView(request, id):
    try:
        obj = Invoice.objects.get(account_type_id=id)
        name = str(obj)
        obj.delete()
        return render(request, 'delete_success.html', {'object':'Invoice', 'name':name})
    except:
        return render(request, 'delete_success.html', {'object':'e', 'name':'error'})

@login_required(login_url='login')
def invoice_list_view(request):
    invoices = Invoice.objects.all()
    return render(request,'Invoice/invoice_list.html',{'invoices':invoices})


#Servicetype views......................................................................................
@login_required(login_url='login')
def AddServiceTypeView(request):
    if request.method == 'POST':
        serviceTypeForm = ServiceTypeForm(request.POST or None)
        if serviceTypeForm.is_valid():
            serviceTypeForm.save()
        return redirect('added')
    else:
        serviceTypeForm = ServiceTypeForm(request.POST or None)
        return render(request, 'Client/add-service.html', {'form': serviceTypeForm})

@login_required(login_url='login')
def UpdateServiceTypeView(request, id):
    service = get_object_or_404(ServiceType, pk=id)
    serviceTypeForm = ServiceTypeForm(request.POST or None, instance=service)
    if serviceTypeForm.is_valid():
        serviceTypeForm.save()
    return render(request, 'Client/add-service.html', {'form': serviceTypeForm})

@login_required(login_url='login')
def DeleteServiceTypeView(request, id):
    try:
        obj = ServiceType.objects.get(account_type_id=id)
        name = str(obj)
        obj.delete()
        return render(request, 'delete_success.html', {'object':'ServiceType', 'name':name})
    except:
        return render(request, 'delete_success.html', {'object':'e', 'name':'error'})
