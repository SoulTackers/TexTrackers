from django import forms
from crispy_forms.helper import FormHelper
from .models import Feesinward,PaymentType




class FeesinwardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        
    class Meta:
        model=Feesinward
        fields = [
            'feesinward_id',
            'feesinward_date',
            'feesinward_inward_mode_id',
            'feesinward_employee_id', 
            'feesinward_discount', 
            'feesinward_balance_outstanding', 
            'feesinward_paymentdetails', 
            'feesinward_paymenttype', 
            'feesinward_amount',
            'feesinward_client_id'
        ]

class PaymenttypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        
    class Meta:
        model=PaymentType
        fields = [
            'paymenttype_details',
            'paymenttype_name'
        ]
