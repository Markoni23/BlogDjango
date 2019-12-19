# Generated by Django 3.0 on 2019-12-19 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20191218_1950'),
        ('posts', '0002_auto_20191218_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='readed_by',
            field=models.ManyToManyField(blank=True, related_name='readed_posts', to='accounts.Account'),
        ),
    ]