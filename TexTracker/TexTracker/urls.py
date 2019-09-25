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
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='Authentication/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Authentication/logout.html'), name='logout'),
    path('authentication/', include('Authentication.urls')),
    path('client/', include('client.urls')),
    path('employee/', include('Employee.urls')),
    path('feesinward/', include('feesinward.urls')),
    path('invoice/', include('invoice.urls')),
    path('inward/', include('inward.urls')),
    path('outward/', include('outward.urls')),
    path('pendingwork/', include('pendingwork.urls')),
]
