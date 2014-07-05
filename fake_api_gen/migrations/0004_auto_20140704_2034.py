# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fake_api_gen', '0003_auto_20140621_1727'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fakeapi',
            options={'permissions': ((b'view_fakeapi', b'View fake api'),)},
        ),
    ]
