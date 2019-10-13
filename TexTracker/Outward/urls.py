from django.urls import path
from .views import outward_view, outward_update, DeleteOutwardView,outward_list_view


urlpatterns = [
    path('listoutward/outward/addoutward',outward_view,name='add-outward'),
    path('listoutward/outward/<int:id>/update',outward_update,name='update-outward'),
    path('listoutward/outward/<int:id>/delete',DeleteOutwardView,name='delete-outward'),
    path('listoutward/',outward_list_view,name='list-outward'),

]
