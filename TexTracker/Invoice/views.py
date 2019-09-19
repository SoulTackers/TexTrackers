# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import InvoiceForm
from django.shortcuts import render

# Create your views here.
def Invoice_view(request):
    form = InvoiceForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request,'Invoice/invoice.html',context)