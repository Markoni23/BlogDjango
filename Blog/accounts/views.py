from django.shortcuts import render
from .models import Account
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class AccountListView(ListView):
    queryset = Account.objects.all()
    context_object_name = 'accounts'
    template_name = 'accounts/accounts.html'