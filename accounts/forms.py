# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms

# settings.py에 등록(설정)된 AUTH_USER_MODEL 변수의 객체를 반환.
from django.contrib.auth import get_user_model 
from .models import CustomUser

# 사용자 등록 Form
# UserCreationForm - ModelForm

class CustomUserCreationForm(UserCreationForm):
    password1=forms.CharField(label='Password', 
                              strip=False,
                              widget=forms.PasswordInput(attrs={'class':'form-control'}))
                              

    password2=forms.CharField(label='Password 확인', 
                              strip=False,
                              widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = CustomUser
        # model = get_user_model()
        fields = ('username', "password1","password2", 'name', 'email', 'gender')
        widgets = {
            "username":forms.TextInput(attrs={"class":"form-control"}),
            'name':forms.TextInput(attrs={"class":"form-control"}),
            'email':forms.EmailInput(attrs={"class":"form-control"}), 
            'gender':forms.Select(attrs={"class":"form-control"}),
        }

# 로그인 Form 재정의
from django.contrib.auth.forms import AuthenticationForm
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='계정', 
                               widget=forms.TextInput(attrs={'class':"form-control"}))
    password = forms.CharField(label='비밀번호',
                              strip=False,
                              widget=forms.PasswordInput(attrs={'class':"form-control"}))    
                              

