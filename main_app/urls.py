from django.urls import path
from .views import *


app_name = "social"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path('profile_list/',profile_list, name='profile_list'),
    path('profile/<int:pk>/', profile, name='profile'),
    path('profile/<int:pk>/update', ProfileUpdate.as_view(), name='profile_update'),
    path('profile/<int:pk>/delete', ProfileDelete.as_view(), name='profile_delete'),
    path('accounts/signup/', signup, name='signup'),
    path('about/', about, name='about'),

]