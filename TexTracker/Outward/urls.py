from django.urls import path
from .views import outward_view, outward_update, DeleteOutwardView


urlpatterns = [
    path('',outward_view,name='add-outward'),
    path('<int:id>/update',outward_update,name='update-outward'),
    path('<int:id>/delete',DeleteOutwardView,name='delete-outward'),
]
