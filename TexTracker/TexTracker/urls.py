"""TexTracker URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from Employee.views import Employee_view
from FeesInward.views import feesinward_view,feesinward_update_view
from Invoice.views import invoice_view,invoice_update_view
from Outward.views import outward_view,outward_update
from PendingWork.views import pendingwork_view,pendingwork_update_view,dashboard
from Inward.views import Inward_view,Inward_update_view
from Client.views import AddClientView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    # path('authentication/', include('Authentication.urls')),
    path('client/', include('Client.urls')),
    path('employee/', include('Employee.urls')),
    path('feesinward/', include('FeesInward.urls')),
    path('invoice/', include('Invoice.urls')),
    path('inward/', include('Inward.urls')),
    path('outward/', include('Outward.urls')),
    path('pendingwork/', include('PendingWork.urls')),
    path('restapi/', include('RestApi.urls')),
    path('dashboard/',dashboard,name='dashboard'),




    # path('admin/', admin.site.urls),
    # path('client/',AddClientView),
    # path('feesinward/',feesinward_view,name='add-feeinward'),
    # path('feesinward/<int:id>/',feesinward_update_view,name='update-feeinward'),
    # path('employee/',Employee_view),
    # path('invoice/',invoice_view,name='add-invoice'),
    # path('invoice/<int:id>',invoice_update_view,name='update-invoice'),
    # path('inward/',Inward_view,name='add-inward'),
    # path('inward/<int:id>',Inward_update_view,name='update-inward'),

    # path('outward/',outward_view,name='add-outward'),
    # path('outward/<int:id>/',outward_update,name='update-outward'),
    # path('pendingwork/',pendingwork_view,name='add-pendingwork'),
    # path('pendingwork/<int:id>/',pendingwork_update_view,name='update-pendingwork'),
    # path('login/', LoginView.as_view(template_name='Authentication/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(template_name='Authentication/logout.html'), name='logout'),
    # path('employee/', include('Employee.urls')),
    # path('',dashboard),
    # path('Authentication/', include('Authentication.urls')),
]