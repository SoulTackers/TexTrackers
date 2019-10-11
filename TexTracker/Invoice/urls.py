from django.urls import path
from .views import invoice_view,invoice_update_view, DeleteInvoiceView
from .views import AddServiceTypeView, UpdateServiceTypeView, DeleteServiceTypeView



urlpatterns = [
    path('addinvoice',invoice_view,name='add-invoice'),
    path('<int:id>/update',invoice_update_view,name='update-invoice'),
    path('<int:id>/delete',DeleteInvoiceView,name='delete-invoice'),
    path('servicetype/addservicetype/', AddServiceTypeView, name='add-servicetype'),
    path('servicetype/<int:id>/update/', UpdateServiceTypeView, name='update-invoice-servicetype'),
    path('servicetype/<int:id>/delete/', DeleteServiceTypeView, name='delete-invoice-servicetype'),
]
