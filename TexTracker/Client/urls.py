from django.conf.urls import url
from .views import  AddClientView
urlpatterns = [
        url('addclient/', AddClientView, name='add-client'),
    ]