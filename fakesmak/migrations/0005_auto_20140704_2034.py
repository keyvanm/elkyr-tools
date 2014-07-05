# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fakesmak', '0004_auto_20140704_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='downvotes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='upvotes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
