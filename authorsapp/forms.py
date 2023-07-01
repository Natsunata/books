from typing import Any
from authorsapp.models import Author
from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4', 'placeholder':'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control py-4', 'placeholder':'Введите пароль'}))
    
    class Meta:
        model = Author
        firlds = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4', 'placeholder':'Введите имя и фимилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4', 'placeholder':'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control py-4', 'placeholder':'Введите адрес эл. почты'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control py-4', 'placeholder':'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control py-4', 'placeholder':'Подтвердите пароль'}))
    
    class Meta:
        model = Author
        fields = ('full_name', 'username','email', 'password1', 'password2')

class UserProfileForm(UserChangeForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'custom-file-label'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4', 'readonly':True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control py-4', 'readonly':True}))
    class Meta:
        model = Author
        fields = ('full_name', 'image', 'username','email')
