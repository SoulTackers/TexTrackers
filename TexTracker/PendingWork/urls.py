from django.urls import path
from PendingWork.views import pendingwork_view,pendingwork_update_view


urlpatterns = [
    path('',pendingwork_view,name='add-pendingwork'),
    path('<int:id>/update',pendingwork_update_view,name='update-pendingwork'),
]