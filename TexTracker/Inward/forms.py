from django import forms
from crispy_forms.helper import FormHelper
from .models import Inward,InwardTypes,InwardPostType,InwardDocument

class InwardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
    class Meta:
        model=Inward
        fields = [
                'inward_id' ,
                #'inward_mode_id',
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
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

class InwardDocumentForm(forms.ModelForm):
    class Meta:
        model=InwardDocument
        fields = [
            'inward_id',
            'inward_doc',
        ]
