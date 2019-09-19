from django import forms
from .models import PendingWork

class PendingWorkForm(forms.ModelForm):
    class Meta:
        model=PendingWork
        fields = [
                'PendingWork_employeeid',
                'PendingWork_inwardid' ,
                'PendingWork_name',
                'PendingWork_postid' 
        ]