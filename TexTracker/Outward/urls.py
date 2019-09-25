from django.urls import path
from Outward.views import outward_view,outward_update


urlpatterns = [
    path('',outward_view,name='add-outward'),
    path('<int:id>/update',outward_update,name='update-outward'),
]
