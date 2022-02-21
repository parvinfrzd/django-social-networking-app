from django.urls import path
from .views import *


app_name = "social"

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('about/', about, name='about'),
    
    path('accounts/signup/', signup, name='signup'),
    
    path('profile_list/',profile_list, name='profile_list'),
    path('profile/<int:pk>/', profile, name='profile'),
    path('profile/<int:pk>/update', ProfileUpdate.as_view(), name='profile_update'),
    path('profile/<int:pk>/delete', ProfileDelete.as_view(), name='profile_delete'),
    
    path('posts/', PostList.as_view(), name='posts_index'),
    path('posts/new/', PostCreate.as_view(), name='posts_create'),
    path('posts/<int:pk>/update/', PostUpdate.as_view(), name='posts_update'),
    path('posts/<int:post_id>', show, name='show'),
    path('posts/<int:pk>/delete/', PostDelete.as_view(), name='posts_delete'),
    path('comments/<int:pk>/update/', CommentUpdate.as_view(), name='comment_update'),
    path('comments/<int:pk>/delete/', CommentDelete.as_view(), name='comment_delete'),


]