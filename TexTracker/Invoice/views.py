# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404,render_to_response
from .forms import InvoiceForm
from django.shortcuts import render
from .models import Invoice

# Create your views here.
def invoice_view(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = InvoiceForm(request.POST or None)
    context = {
        'form' : form
    }
    return render(request,'Invoice/invoice.html',context)

def invoice_update_view(request,id):
    invoice = get_object_or_404(Invoice,outward_id=id)
    invoice_update_form = InvoiceForm(request.POST or None,instance=invoice)

    if invoice_update_form.is_valid():
        invoice_update_form.save()
    
    return render(request,'Invoice/invoice.html',{'form':invoice_update_form})