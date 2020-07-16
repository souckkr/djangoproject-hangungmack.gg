from django.urls import path

from . import views

from django.contrib.auth.views import LogoutView
# accounts/urls.py
app_name = 'accounts'



urlpatterns = [
    path('join', views.UserCreateView.as_view(), name='join'),
    path('login', views.CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
