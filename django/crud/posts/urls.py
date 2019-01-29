from django.urls import path, include
from . import views

urlpatterns = [
    path('naver/<str:q>/', views.naver),
    path('', views.index),
    path('create/', views.create),
    path('new/', views.new),
    path('<int:post_id>/', views.detail),  #view의 변수이름과 동일하게.
    path('<int:post_id>/delete/', views.delete),
    path('<int:post_id>/edit/', views.edit),
    path('<int:post_id>/update/', views.update),
]
