from django.urls import path
from .views import feesinward_view,feesinward_update_view
from .views import AddPaymentTypeView, UpdatePaymentTypeView, DeletePaymentTypeView



urlpatterns = [
    path('',feesinward_view,name='add-feeinward'),
    path('<int:id>/update',feesinward_update_view,name='update-feeinward'),
    path('paymenttype/addpaymenttype/', AddPaymentTypeView, name='add-paymenttype'),
    path('paymenttype/<int:id>/update/', UpdatePaymentTypeView, name='update-paymenttype'),
    path('paymenttype/<int:id>/delete/', DeletePaymentTypeView, name='delete-paymenttype'),
]
