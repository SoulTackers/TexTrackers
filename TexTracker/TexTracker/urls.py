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
from django.contrib import admin
from Employee.views import Employee_view
from FeesInward.views import Feesinward_view
from Invoice.views import Invoice_view
from Outward.views import Outward_view
from PendingWork.views import PendingWork_view
from Inward.views import Inward_view
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('feesinward/',Feesinward_view),
    url('employeet/',Employee_view),
    url('invoice/',Invoice_view),
    url('inward/',Inward_view),
    url('outward/',Outward_view),
    url('pendingwork/',PendingWork_view),
    url('login/', LoginView.as_view(template_name='Authentication/login.html'), name='login'),
    url('logout/', LogoutView.as_view(template_name='Authentication/logout.html'), name='logout'),
    url(r'^employee/', include('Employee.urls')),
    url(r'^client/', include('Client.urls')),
    url(r'^Authentication/', include('Authentication.urls')),
]
