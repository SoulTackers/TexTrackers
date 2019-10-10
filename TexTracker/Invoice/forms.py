from django import forms
from crispy_forms.helper import FormHelper
from .models import Invoice,Servicetype

class InvoiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

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

class ServicetypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model=Servicetype
        fields = [
            'servicetype_name',
            'servicetype_details' 
        ]