# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20140622_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='contributers',
            new_name='contributors',
        ),
    ]
