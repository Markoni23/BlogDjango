from django.db import models
from accounts.models import Account

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Account, 
                                on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
