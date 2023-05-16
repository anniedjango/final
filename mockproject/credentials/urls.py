from django.urls import path
from . import views


urlpatterns = [

    path('register',views.register,name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('home', views.home, name='home'),
    path('but', views.but, name='but'),
    path('form', views.form, name='form'),
    path('signup_view', views.signup_view, name='signup_view'),
    path('acp', views.acp, name='acp'),





]