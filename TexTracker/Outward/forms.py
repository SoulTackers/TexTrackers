from django import forms
from crispy_forms.helper import FormHelper
from .models import Outward

class OutwardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
    class Meta:
        model=Outward
        fields = [
            'outward_cid',
            'outward_date',
            'outward_uploaddocstatus',
            'outward_iid',
        ]
