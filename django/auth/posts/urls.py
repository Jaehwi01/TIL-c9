from django.urls import path, include
from . import views

app_name = 'posts'
urlpatterns = [
    # path('naver/<str:q>/', views.naver),
    path('', views.index, name='list'), # get
    # path('create/', views.create, name='create'), 
    path('write/', views.new, name='new'), #get(new),#post(create)
    path('<int:post_id>/', views.detail, name='detail'),  #view의 변수이름과 동일하게. #GET
    path('<int:post_id>/delete/', views.delete, name='delete'), #get(confirm). post
    path('<int:post_id>/edit/', views.edit, name='edit'), #get(edit), post(update)
    # path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete'),
]
