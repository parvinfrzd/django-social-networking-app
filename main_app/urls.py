from django.urls import path
from . import views 

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='posts_index'),
    path('posts/new/', views.PostCreate.as_view(), name='posts_create'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='posts_update'),
    path('posts/<int:post_id>/', views.show, name='show'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='posts_delete'),
    path('posts/<int:pk>/like/', views.AddLike.as_view(), name='like'),
    path('posts/<int:pk>/dislike/', views.AddDislike.as_view(), name='dislike'),
]