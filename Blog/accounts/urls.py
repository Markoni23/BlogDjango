from django.urls import path
from .views import *


urlpatterns = [
    path('', AccountListView.as_view()),
]