from django.urls import path
from Inward.views import Inward_view,Inward_update_view


urlpatterns = [
    path('',Inward_view,name='add-inward'),
    path('<int:id>/update',Inward_update_view,name='update-inward')
]
