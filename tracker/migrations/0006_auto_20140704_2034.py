# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20140624_2128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': ((b'view_project', b'Can view project'), (b'all_project', b'All permissions project'))},
        ),
        migrations.AlterModelOptions(
            name='story',
            options={'ordering': [b'due_date'], 'verbose_name_plural': b'stories', 'permissions': ((b'view_story', b'Can view stories'), (b'all_story', b'All permissions story'))},
        ),
    ]
