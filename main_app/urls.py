from django.urls import path
from .views import *


app_name = "social"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path('about/', about, name='about'),
    
    path('accounts/signup/', signup, name='signup'),
    
    path('profile_list/',profile_list, name='profile_list'),
    path('profile/<int:pk>/', profile, name='profile'),
    path('profile/<int:pk>/update', ProfileUpdate.as_view(), name='profile_update'),
    path('profile/<int:pk>/delete', ProfileDelete.as_view(), name='profile_delete'),
    
    path('posts/', PostList.as_view(), name='posts_index'),
    path('posts/<int:post_id>/add_comment/', add_comment, name='add_comment'),
    path('posts/<int:post_id>/comments/<int:comment_id>', delete_comment, name='comment_delete'),
    path('posts/new/', PostCreate.as_view(), name='posts_create'),
    path('posts/<int:pk>/update/', PostUpdate.as_view(), name='posts_update'),
    path('posts/<int:post_id>', posts_detail, name='posts_detail'),
    path('posts/<int:pk>/delete/', PostDelete.as_view(), name='posts_delete'),
]