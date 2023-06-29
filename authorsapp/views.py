from django.shortcuts import render
from common.views import TitleMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from authorsapp.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from authorsapp.models import Author
from django.urls import reverse, reverse_lazy


class UserLoginView(TitleMixin, LoginView):
    template_name = 'authorsapp/login.html'
    form_class = UserLoginForm
    title = 'Books - Авторизация'

class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = Author
    form_class = UserRegistrationForm
    template_name = 'authorsapp/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрированы!'
    title = 'Books - Регистрация'

class UserProfileView(TitleMixin, UpdateView):
    model = Author
    form_class = UserProfileForm
    template_name = 'authorsapp/profile.html'
    title = 'Books - Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    