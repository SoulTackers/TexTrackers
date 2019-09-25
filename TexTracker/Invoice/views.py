# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404,render_to_response
from .forms import InvoiceForm,ServicetypeForm
from django.shortcuts import render
from .models import Invoice,Servicetype

# Create your views here.
def invoice_view(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST or None)
        form1 = ServicetypeForm(request.POST or None)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
    else:
        form = InvoiceForm(request.POST or None)
        form1 = ServicetypeForm(request.POST or None)
    context = {
        'form' : form,
        'servicetype_form' : form1
    }
    return render(request,'Invoice/invoice.html',context)

def invoice_update_view(request,id):
    invoice = get_object_or_404(Invoice,outward_id=id)
    servicetype = get_object_or_404(Servicetype,servicetype_id=id)
    invoice_update_form = InvoiceForm(request.POST or None,instance=invoice)
    servicetype_update_form = ServicetypeForm(request.POST or None,instance=servicetype)

    if invoice_update_form.is_valid() and servicetype_update_form.is_valid():
        invoice_update_form.save()
        servicetype_update_form.save()
    
    return render(request,'Invoice/invoice.html',{'form':invoice_update_form,'servicetype_form' : servicetype_update_form})