from django.urls import path
from Inward.views import Inward_view


urlpatterns = [
    path('',Inward_view,name='add-inward'),
]
