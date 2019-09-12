from django import forms

from .models import Inward

class InwardForm(forms.ModelForm):
    class Meta:
        model=Inward
        fields = [
                'inward_id' ,
                'inward_mode_id' ,
                'inward_track',
                'inward_employeeid',
                'inward_posttype' ,
                'inward_returnperiod',
                'inward_month' ,
                'inward_year' ,
                'inward_remarks',
                'inward_client_id',
                'inward_date'
        ]