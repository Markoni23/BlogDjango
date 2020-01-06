from django.urls import path
from .views import *


urlpatterns = [
    path('', AccountListView.as_view(), name='profiles'),
    path('<int:pk>', AccountDetailView.as_view(), name='profile'),
    path('follow/<int:pk>', follow, name='follow'),
    path('disfollow/<int:pk>', dis_follow, name='dis_follow'),
    path('post_for_user/<int:pk>', PostForUser.as_view(), name='post_for_user'),
    path('post_by_user/<int:pk>', PostByUser.as_view(), name='post_by_user'),
]