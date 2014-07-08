# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import fakesmak.models.userprofile


class Migration(migrations.Migration):

    dependencies = [
        ('fakesmak', '0006_auto_20140704_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(upload_to=fakesmak.models.userprofile.unique_filename, blank=True),
        ),
    ]
