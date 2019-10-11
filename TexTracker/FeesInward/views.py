# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import FeesinwardForm,PaymenttypeForm
from django.shortcuts import render,get_object_or_404,render_to_response
from django.shortcuts import render
from .models import Feesinward,PaymentType
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def feesinward_view(request):
    if request.method == 'POST':
        form = FeesinwardForm(request.POST or None)
        form1 = PaymenttypeForm(request.POST or None)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
    else:
        form = FeesinwardForm()
        form1 = PaymenttypeForm()
    
    context = {
        'form' : form,
        'payment_form':form1
    }
    return render(request,'FeesInward/feesinward.html',context)

@login_required(login_url='login')
def feesinward_update_view(request,id):
    feesinward = get_object_or_404(Feesinward,outward_id=id)
    paymenttype = get_object_or_404(PaymentType,paymenttype_id=id)
    feesinward_update_form = FeesinwardForm(request.POST or None,instance=feesinward)
    paymenttype_update_form = PaymenttypeForm(request.POST or None,instance=paymenttype)

    if feesinward_update_form.is_valid() and paymenttype_update_form.is_valid():
        feesinward_update_form.save()
        paymenttype_update_form.save()
    
    return render(request,'FeesInward/feesinward.html',{'form':feesinward_update_form,'payment_form':paymenttype_update_form})


@login_required(login_url='login')
def feesinward_list_view(request):
    feesinwards = Feesinward.objects.all()
    return render(request,'FeesInward/feesinward_list.html',{'feesinwards':feesinwards})



# PaymentType views.....................................................................................
@login_required(login_url='login')
def AddPaymentTypeView(request):
    if request.method == 'POST':
        paymentTypeForm = PaymentTypeForm(request.POST or None)
        if paymentTypeForm.is_valid():
            paymentTypeForm.save()
        return redirect('added')
    else:
        paymentTypeForm = PaymentTypeForm(request.POST or None)
        return render(request, 'Client/add-service.html', {'form': paymentTypeForm})

@login_required(login_url='login')
def UpdatePaymentTypeView(request, id):
    service = get_object_or_404(PaymentType, pk=id)
    paymentTypeForm = PaymentTypeForm(request.POST or None, instance=service)
    if paymentTypeForm.is_valid():
        paymentTypeForm.save()
    return render(request, 'Client/add-service.html', {'form': paymentTypeForm})

@login_required(login_url='login')
def DeletePaymentTypeView(request, id):
    try:
        obj = PaymentType.objects.get(account_type_id=id)
        name = str(obj)
        obj.delete()
        return render(request, 'delete_success.html', {'object':'PaymentType', 'name':name})
    except:
        return render(request, 'delete_success.html', {'object':'e', 'name':'error'}) 
