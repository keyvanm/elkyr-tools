# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20140621_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 6, 22, 13, 50, 9, 16478), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 6, 22, 13, 50, 25, 561642), auto_now_add=True),
            preserve_default=False,
        ),
    ]
