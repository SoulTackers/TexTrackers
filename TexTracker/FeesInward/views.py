# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import FeesinwardForm,PaymenttypeForm
from django.shortcuts import render,get_object_or_404,render_to_response
from django.shortcuts import render
from .models import Feesinward,PaymentType

# Create your views here.
def feesinward_view(request):
    if request.method == 'POST':
        form = FeesinwardForm(request.POST or None)
        form1 = PaymenttypeForm(request.POST or None)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
    else:
        form = FeesinwardForm(request.POST or None)
        form1 = PaymenttypeForm(request.POST or None)
    
    context = {
        'form' : form,
        'payment_form':form1
    }
    return render(request,'FeesInward/feesinward.html',context)

def feesinward_update_view(request,id):
    feesinward = get_object_or_404(Feesinward,outward_id=id)
    paymenttype = get_object_or_404(PaymentType,paymenttype_id=id)
    feesinward_update_form = FeesinwardForm(request.POST or None,instance=feesinward)
    paymenttype_update_form = PaymenttypeForm(request.POST or None,instance=paymenttype)

    if feesinward_update_form.is_valid() and paymenttype_update_form.is_valid():
        feesinward_update_form.save()
        paymenttype_update_form.save()
    
    return render(request,'FeesInward/feesinward.html',{'form':feesinward_update_form,'payment_form':paymenttype_update_form})