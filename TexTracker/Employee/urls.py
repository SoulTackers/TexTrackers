from django.conf.urls import url
from .views import AddEmployeeView

urlpatterns = [
        url('addemployee/',AddEmployeeView, name='add-employee'),
    ]
