# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=80)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('forum', models.ForeignKey(to='forum.Forum')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(to='forum.Thread'),
        ),
    ]
