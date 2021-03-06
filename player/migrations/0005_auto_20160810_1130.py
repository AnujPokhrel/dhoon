# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-10 11:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('player', '0004_auto_20160809_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='song',
            name='rating',
        ),
        migrations.AddField(
            model_name='rating',
            name='song',
            field=models.ManyToManyField(default=1, related_name='song_star', to='player.Song'),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ManyToManyField(default=1, related_name='song_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
