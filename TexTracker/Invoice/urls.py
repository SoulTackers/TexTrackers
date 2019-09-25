from django.urls import path
from Invoice.views import invoice_view,invoice_update_view


urlpatterns = [
    path('',invoice_view,name='add-invoice'),
    path('<int:id>/update',invoice_update_view,name='update-invoice'),
]
