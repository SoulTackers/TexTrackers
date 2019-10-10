from django import forms
from crispy_forms.helper import FormHelper
from .models import Employee,EmployeePost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
    class Meta:
        model=Employee
        fields = [
            'employee_name',
            'employee_postid',
            'employee_phone',
        ]
        labels = {
            'employee_name' : 'Employee Name',
            'employee_postid' : 'Employee Post',
            'employee_phone' : 'Employee Phone'

        }


class AdminEmployeeAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
    class Meta:
        model=User
        fields = [
            'username',
        ]

        


class EmployeePostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
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

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']