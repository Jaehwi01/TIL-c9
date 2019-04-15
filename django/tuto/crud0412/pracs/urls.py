from django.contrib import admin
from django.urls import path,include
from . import views

app_name='pracs'
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:prac_id')
]