# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import CreateView, UpdateView
from django.shortcuts import render
from .models import AccountType, Client, ClientAccountantInfo, ClientBankInfo, ClientLegalInfo, ClientPassword, ClientSevice
from .forms import (AccountTypeForm,
                    ClientAccountantInfoForm,
                    ClientBankInfoForm,
                    ClientForm,
                    ClientLegalInfoForm,
                    ClientPasswordForm,
                    ClientSeviceForm)

# Create your views here.
def AddClientView(request):

    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        clientBankInfo_Form = ClientBankInfoForm(request.POST)
        clientAccountantInfo_Form = ClientAccountantInfoForm(request.POST)
        clientLegalInfo_Form = ClientLegalInfoForm(request.POST)
        clientPassword_Form = ClientPasswordForm(request.POST)
        clientSevice_Form = ClientSeviceForm(request.POST)
        if ( client_form.is_valid()
             and clientAccountantInfo_Form.is_valid()
             and clientBankInfo_Form.is_valid()
             and clientLegalInfo_Form.is_valid()
             and clientPassword_Form.is_valid()
             and clientSevice_Form.is_valid()):

             client = client_form.save()
             form_list = []
             form_list.append(clientAccountantInfo_Form.save(commit=False))
             form_list.append(clientBankInfo_Form.save(commit=False))
             form_list.append(clientLegalInfo_Form.save(commit=False))
             form_list.append(clientPassword_Form.save(commit=False))
             form_list.append(clientSevice_Form.save(commit=False))

             for form in form_list:
                if form.client is None:
                     form.client = client
                form.save()
        
    else:
        client_form = ClientForm()
        clientBankInfo_Form = ClientBankInfoForm()
        clientAccountantInfo_Form = ClientAccountantInfoForm()
        clientLegalInfo_Form = ClientLegalInfoForm()
        clientPassword_Form = ClientPasswordForm()
        clientSevice_Form = ClientSeviceForm()


    context = {
            'client_form': client_form,
            'clientBankInfo_Form': clientBankInfo_Form,
            'clientAccountantInfo_Form': clientAccountantInfo_Form,
            'clientLegalInfo_Form': clientLegalInfo_Form,
            'clientPassword_Form': clientPassword_Form,
            'clientSevice_Form': clientSevice_Form,
        }
    return render(request, 'Client/add-client.html', context)   