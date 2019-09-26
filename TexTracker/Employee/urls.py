from django.conf.urls import url
from .views import AddEmployeeView,Employee_view

urlpatterns = [
        url('addemployee/',AddEmployeeView, name='add-employee'),
        url('',Employee_view,name='employee')
    ]
