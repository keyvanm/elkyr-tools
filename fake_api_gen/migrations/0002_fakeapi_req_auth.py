# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fake_api_gen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fakeapi',
            name='req_auth',
            field=models.BooleanField(default=True, verbose_name=b'Require Authentication?'),
            preserve_default=True,
        ),
    ]
