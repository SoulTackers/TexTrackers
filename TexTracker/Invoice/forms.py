from django import forms

from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model=Invoice
        fields = [
            'invoice_id',
            'invoice_servicetype',
            'invoice_address',
            'invoice_amount' ,
            'invoice_comments',
            'invoice_clientid', 
            'invoice_date' 
        ]