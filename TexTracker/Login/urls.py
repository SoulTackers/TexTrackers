from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import url

urlpatterns=[
    url('login', LoginView.as_view(template_name='Login/login.html'), name='login'),
    url('logout', LogoutView.as_view(template_name='Login/logout.html'), name='logout'),

]
