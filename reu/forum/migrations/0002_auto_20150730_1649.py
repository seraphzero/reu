# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel('Thread', 'Topic'),
        migrations.RenameField('Post', 'thread', 'topic')
    ]
