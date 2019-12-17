from django.urls import path
from .views import *
urlpatterns = [
    path('', PostsListView.as_view()),
]