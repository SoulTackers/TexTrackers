from django.urls import path
from FeesInward.views import feesinward_view,feesinward_update_view


urlpatterns = [
    path('',feesinward_view,name='add-feeinward'),
    path('<int:id>/update',feesinward_update_view,name='update-feeinward'),
]
