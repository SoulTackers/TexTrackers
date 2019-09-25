from django.conf.urls import url
from django.urls import path
from .views import AddEmployeeView,Employee_view, UpdateEmployeeView

urlpatterns = [
        url('addemployee/',AddEmployeeView, name='add-employee'),
        url('',Employee_view,name='employee'),
        path('<int:id>/ue/',UpdateEmployeeView,name='employee-update'),
    ]
