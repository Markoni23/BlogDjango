from django.urls import path
from .views import *


urlpatterns = [
    path('', PostsListView.as_view(), name='posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
]