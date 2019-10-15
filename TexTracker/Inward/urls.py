from django.urls import path
from .views import Inward_view,Inward_update_view,inward_pass, DeleteInwardView,inward_list_view
from .views import AddInwardTypesView, UpdateInwardTypesView, DeleteInwardTypesView,AdddocumentView
from .views import AddInwardPostTypesView, UpdateInwardPostTypesView, DeleteInwardPostTypesView,pass_inward_real



urlpatterns = [
    path('addinward',Inward_view,name='add-inward'),
    path('<int:id>/pinward/',pass_inward_real,name='pass-inward'),
    path('listinwards/inward/<int:id>/update',Inward_update_view,name='update-inward'),
    path('listinwards/inward/<int:id>/delete',DeleteInwardView,name='delete-inward'),
    path('<int:id>/show',inward_pass,name='show-inward'),
    path('inwardtypes/addinwardtypes/', AddInwardTypesView, name='add-inwardtypes'),
    path('inwardtypes/<int:id>/update/', UpdateInwardTypesView, name='update-inwardtypes'),
    path('inwardtypes/<int:id>/delete/', DeleteInwardTypesView, name='delete-inwardtypes'),
    path('inwardposttypes/addinwardposttypes/', AddInwardPostTypesView, name='add-inwardposttypes'),
    path('inwardposttypes/<int:id>/update/', UpdateInwardPostTypesView, name='update-inwardposttypes'),
    path('inwardposttypes/<int:id>/delete/', DeleteInwardPostTypesView, name='delete-inwardposttypes'),
    path('listinwards/', inward_list_view, name='list-inward'),
    path('docupload/', AdddocumentView, name='add-doc-view')
]
