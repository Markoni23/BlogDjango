from django.shortcuts import render, redirect
from .models import Account
from posts.models import Post
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


def follow(request, pk):
    reader = request.user.account
    reader.folowers.add(Account.objects.get(pk=pk))
    return redirect('post_by_user', pk=reader.pk)

def dis_follow(request, pk):
    reader = request.user.account
    reader.folowers.remove(Account.objects.get(pk=pk))
    return redirect('post_by_user', pk=reader.pk)


class AccountListView(LoginRequiredMixin, ListView):
    queryset = Account.objects.all()
    context_object_name = 'accounts'
    template_name = 'accounts/accounts.html'

class AccountDetailView(LoginRequiredMixin, DetailView):
    model = Account

class PostByUser(LoginRequiredMixin, ListView):
    template_name = 'posts/posts.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        try:
            user = Account.objects.get(pk=self.kwargs['pk'])
            return Post.objects.filter(author__in=user.folowers.all()).order_by('-created')
        except:
            return Post.objects.none()