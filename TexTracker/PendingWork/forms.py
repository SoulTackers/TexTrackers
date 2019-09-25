from django import forms
from .models import PendingWork
from crispy_forms.helper import FormHelper
class PendingWorkForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
    class Meta:
        model=PendingWork
        fields = [
                'PendingWork_employeeid',
                'PendingWork_inwardid' ,
                'PendingWork_name',
                'PendingWork_postid' 
        ]