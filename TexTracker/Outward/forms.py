from django import forms

from .models import Outward

class OutwardForm(forms.ModelForm):
    class Meta:
        model=Outward
        fields = [
            'outward_id' ,
            'outward_clientid', 
            'outward_date', 
            'outward_uploaddocstatus',
            'outward_inwardid'
        ]