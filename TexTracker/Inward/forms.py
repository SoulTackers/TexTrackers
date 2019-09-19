from django import forms

from .models import Inward,InwardTypes,InwardPostType

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

class InwardPostTypeForm(forms.ModelForm):
    class Meta:
        model=InwardPostType
        fields = [
                'InwardPostType_name',
                'InwardPostType_details'
        ]


class InwardTypesForm(forms.ModelForm):
    class Meta:
        model=InwardTypes
        fields = [
                'InwardTypes_name' ,
                'InwardTypes_details' 
        ]