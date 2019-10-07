from django.urls import path
from .views import Inward_view,Inward_update_view,inward_pass
from .views import AddInwardTypesView, UpdateInwardTypesView, DeleteInwardTypesView
from .views import AddInwardPostTypesView, UpdateInwardPostTypesView, DeleteInwardPostTypesView



urlpatterns = [
    path('addinward',Inward_view,name='add-inward'),
    path('<int:id>/update',Inward_update_view,name='update-inward'),
    path('<int:id>/show',inward_pass,name='show-inward'),
    path('inwardtypes/addinwardtypes/', AddInwardTypesView, name='add-inwardtypes'),
    path('inwardtypes/<int:id>/update/', UpdateInwardTypesView, name='update-inwardtypes'),
    path('inwardtypes/<int:id>/delete/', DeleteInwardTypesView, name='delete-inwardtypes'),
    path('inwardposttypes/addinwardposttypes/', AddInwardPostTypesView, name='add-inwardposttypes'),
    path('inwardposttypes/<int:id>/update/', UpdateInwardPostTypesView, name='update-inwardposttypes'),
    path('inwardposttypes/<int:id>/delete/', DeleteInwardPostTypesView, name='delete-inwardposttypes'),
]
