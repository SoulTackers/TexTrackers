# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import CreateView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
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

def UpdateClientView(request, id):

    client = get_object_or_404(Client, client_id=id)
    client_form = ClientForm(request.POST or None, instance=client)

    clientBankInfo = get_object_or_404(ClientBankInfo, client=id)
    clientBankInfo_Form = ClientBankInfoForm(request.POST or None, instance=clientBankInfo)

    clientAccountantInfo = get_object_or_404(ClientAccountantInfo, client=id)
    clientAccountantInfo_Form = ClientAccountantInfoForm(request.POST or None, instance=clientAccountantInfo)

    clientLegalInfo = get_object_or_404(ClientLegalInfo, client=id)
    clientLegalInfo_Form = ClientLegalInfoForm(request.POST or None, instance=clientLegalInfo)

    clientPassword = get_object_or_404(ClientPassword, client=id)
    clientPassword_Form = ClientPasswordForm(request.POST or None, instance=clientPassword)

    clientSevice = get_object_or_404(ClientSevice, client=id)
    clientSevice_Form = ClientSeviceForm(request.POST or None, instance=clientSevice)

    if ( client_form.is_valid()
          and clientAccountantInfo_Form.is_valid()
          and clientBankInfo_Form.is_valid()
          and clientLegalInfo_Form.is_valid()
          and clientPassword_Form.is_valid()
          and clientSevice_Form.is_valid()):
          
          client = client_form.save()
          clientBankInfo_Form = clientBankInfo_Form.save()
          clientAccountantInfo_Form = clientAccountantInfo_Form.save()
          clientLegalInfo_Form = clientLegalInfo_Form.save()
          clientPassword_Form = clientPassword_Form.save()
          clientSevice_Form = clientSevice_Form.save()

          return redirect('login')

    context = {
            'client_form': client_form,
            'clientBankInfo_Form': clientBankInfo_Form,
            'clientAccountantInfo_Form': clientAccountantInfo_Form,
            'clientLegalInfo_Form': clientLegalInfo_Form,
            'clientPassword_Form': clientPassword_Form,
            'clientSevice_Form': clientSevice_Form,
        }

    return render(request, 'Client/add-client.html', context)
