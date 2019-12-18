from django.shortcuts import render
from .models import Post
from accounts.models import Account
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class PostsListView(LoginRequiredMixin, ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'posts/posts.html'
    ordering = ['-created']

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = Account.objects.get(user=self.request.user)
        return super().form_valid(form)


