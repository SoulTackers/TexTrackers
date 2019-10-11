from django.conf.urls import url
from django.urls import path
from .views import AddEmployeeView,Employee_view, UpdateEmployeeView, AdminAddEmployeeView
from .views import AddEmployeePostView, UpdateEmployeePostView, DeleteEmployeePostView

urlpatterns = [
        path('addemployee/',AddEmployeeView, name='add-employee'),
        #url('',Employee_view,name='employee')
        path('update/', UpdateEmployeeView, name='update-employee'),
        path('admin-addemployee/',AdminAddEmployeeView, name='admin-add-employee'),
        path('employeepost/addemployeepost/', AddEmployeePostView, name='add-employeepost'),
        path('employeepost/<int:id>/update/', UpdateEmployeePostView, name='update-employeepost'),
        path('employeepost/<int:id>/delete/', DeleteEmployeePostView, name='delete-employeepost'),
    ]
