from django import forms

from .models import Employee,EmployeePost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
