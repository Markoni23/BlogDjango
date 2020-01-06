from django.urls import path
from .views import *


urlpatterns = [
    path('', PostsListView.as_view(), name='posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/readed/<int:pk>', mark_as_readed, name='post_readed'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]