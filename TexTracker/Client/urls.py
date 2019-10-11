from django.urls import path
from .views import  AddClientView, UpdateClientView, AddServiceView, UpdateServiceView, DeleteServiceView
from .views import  AddAccountTypeView, UpdateAccountTypeView, DeleteAccountTypeView
urlpatterns = [
        path('addclient/', AddClientView, name='add-client'),
        path('<int:id>/update/', UpdateClientView, name='update-client'),
        path('service/addservice/', AddServiceView, name='add-service'),
        path('service/<int:id>/update/', UpdateServiceView, name='update-service'),
        path('service/<int:id>/delete/', DeleteServiceView, name='delete-service'),
        path('accounttype/addaccounttype/', AddAccountTypeView, name='add-accounttype'),
        path('accounttype/<int:id>/update/', UpdateAccountTypeView, name='update-accounttype'),
        path('accounttype/<int:id>/delete/', DeleteAccountTypeView, name='delete-accounttype'),
    ]
