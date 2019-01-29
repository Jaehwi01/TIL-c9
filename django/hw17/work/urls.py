from django.urls import path, include
from . import views

urlpatterns = [
   
    path('', views.index),
    path('create/',views.create),
    path('new/', views.new),
    path('<int:work_id>/', views.detail),
    path('<int:work_id>/delete/', views.delete),
    path('<int:work_id>/edit/', views.edit),
    path('<int:work_id>/update/', views.update),

 
]
