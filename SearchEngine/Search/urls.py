from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'Search'

urlpatterns = [
        path('',views.index, name='index'),
        path('signup/', views.signup, name='signup'),
        path('welcome/', views.welcome, name='welcome'),
        path('login/', auth_views.LoginView.as_view(template_name='Search/login.html',authentication_form=LoginForm), name='login'),
        path('logout/', views.logout_view, name='logout'),
        path('about/', views.about, name='about'),
        path('contact/', views.contact, name='contact'),
    ]