from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User,
                             on_delete=models.CASCADE,
                             related_name = 'account')
    folowers = models.ManyToManyField("self",
                                      related_name='readers',
                                      symmetrical=False,
                                      blank=True)

    def __str__(self):
        return self.user.username
