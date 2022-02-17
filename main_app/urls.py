from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='posts_index'),
    path('posts/new/', views.PostCreate.as_view(), name='posts_create'),
    path('posts/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('posts/<int:post_id>/comments/<int:comment_id>', views.delete_comment, name='comment_delete'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='posts_update'),
    path('posts/<int:post_id>', views.show, name='show'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='posts_delete'),
    path('', views.index, name="index"),
]