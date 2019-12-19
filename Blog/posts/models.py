from django.db import models
from accounts.models import Account
from .utils import send_mail_to_reader


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Account, 
                                on_delete=models.CASCADE)
    readed_by = models.ManyToManyField(Account,
                                related_name='readed_posts',
                                blank = True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        return '/post/%i' % self.id

    def save(self, *args, **kwargs):
        if not self.pk:
            send_mail_to_reader(self)
            super(Post, self).save(*args, **kwargs)