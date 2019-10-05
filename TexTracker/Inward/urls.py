from django.urls import path
from Inward.views import Inward_view,Inward_update_view,inward_pass


urlpatterns = [
    path('addinward',Inward_view,name='add-inward'),
    path('<int:id>/update',Inward_update_view,name='update-inward'),
    path('<int:id>/show',inward_pass,name='show-inward'),

]
