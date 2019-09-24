from django.conf.urls import url
from .views import AddEmployeeView,Employee_view, UpdateEmployeeView

urlpatterns = [
        url('addemployee/',AddEmployeeView, name='add-employee'),
        url('',Employee_view,name='employee'),
        url('ue/',UpdateEmployeeView,name='employee-update'),

    ]
