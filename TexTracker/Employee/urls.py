from django.conf.urls import url
from django.urls import path
from .views import AddEmployeeView,Employee_view, UpdateEmployeeView, AdminAddEmployeeView

urlpatterns = [
        path('addemployee/',AddEmployeeView, name='add-employee'),
        #url('',Employee_view,name='employee')
        path('<int:id>/update/', UpdateEmployeeView, name='update-employee'),
        path('admin-addemployee/',AdminAddEmployeeView, name='admin-add-employee'),
    ]
