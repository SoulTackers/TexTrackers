from django.urls import path
from .views import  AddClientView, UpdateClientView
urlpatterns = [
        path('addclient/', AddClientView, name='add-client'),
        path('<int:id>/update', UpdateClientView, name='update-client'),
    ]