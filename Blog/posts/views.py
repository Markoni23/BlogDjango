from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class PostsListView(LoginRequiredMixin, ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'posts/posts.html'
