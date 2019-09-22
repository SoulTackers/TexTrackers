from django import forms

from .models import Feesinward

class FeesinwardForm(forms.ModelForm):
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