from django.urls import path
from .views import  AddClientView, UpdateClientView, AddServiceView, UpdateServiceView, DeleteServiceView
urlpatterns = [
        path('addclient/', AddClientView, name='add-client'),
        path('<int:id>/update/', UpdateClientView, name='add-client'),
        path('service/addservice/', AddServiceView, name='add-service'),
        path('service/<int:id>/update/', UpdateServiceView, name='update-service'),
        path('service/<int:id>/delete/', DeleteServiceView, name='delete-service'),
    ]