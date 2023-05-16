from django.urls import path
from .import views
app_name='mockapp'
urlpatterns = [

    path('', views.demo, name='demo'),

    ]
