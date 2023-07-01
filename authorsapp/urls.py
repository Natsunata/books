from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import  path
from authorsapp.views import UserLoginView, UserRegistrationView, UserProfileView

app_name = 'authorsapp'


urlpatterns = [
# Auth
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),

]