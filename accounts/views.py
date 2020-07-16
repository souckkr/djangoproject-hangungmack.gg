# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth.views import LoginView

from django.contrib.auth.forms import AuthenticationForm #로그인 Form

from .forms import CustomUserCreationForm, UserLoginForm
# accounts/views.py

# 가입 View
class UserCreateView(CreateView):
    template_name = 'accounts/join_form.html' #가입 폼
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home') #가입처리후 이동할 url-redirect

# 로그인 View
class CustomLoginView(LoginView):
    template_name = "accounts/login_form.html" #로그인 폼 화면
    # form_class = AuthenticationForm
    form_class = UserLoginForm


