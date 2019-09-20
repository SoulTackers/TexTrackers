from django.shortcuts import render

# Create your views here.
from .forms import UserRegisterForm
from Employee.forms import EmployeeForm

def login_employee(request):
    if request.method == 'POST':
        form1 = UserRegisterForm(request.POST)
        form2 = EmployeeForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            new_user = form1.save()
            employee = form2.save(commit=False)
            if employee.user_id is None:
                employee.user_id = new_user.id
            form2.save()
    else:
        form1 = UserRegisterForm()
        form2 = EmployeeForm()
    return render(request, 'Login/login.html', {'form1': form1, 'form2': form2})
