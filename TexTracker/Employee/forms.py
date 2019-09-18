from django import forms

from .models import Employee,EmployeePost

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields = [
            'employee_name',
            'employee_postid',
            'employee_phone',
        ]

class EmployeePostForm(forms.ModelForm):
    class Meta:
        model=EmployeePost
        fields = [
            'ep_details',
            'ep_name',
        ]