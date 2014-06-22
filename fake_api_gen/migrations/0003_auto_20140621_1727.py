# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fake_api_gen', '0002_fakeapi_req_auth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakeapi',
            name='response_status_code',
            field=models.IntegerField(default=200, choices=[(100, b'1xx Informational'), (200, b'2xx Success'), (200, b'3xx Redirection'), (200, b'4xx Client Error'), (200, b'5xx Server Error')]),
        ),
    ]
