# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FakeApi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(to_field='id', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('request_method', models.CharField(default=b'GET', max_length=10, choices=[(b'GET', b'GET'), (b'HEAD', b'HEAD'), (b'POST', b'POST'), (b'PUT', b'PUT'), (b'DELETE', b'DELETE'), (b'OPTIONS', b'OPTIONS'), (b'CONNECT', b'CONNECT'), (b'PATCH', b'PATCH')])),
                ('response_body_type', models.CharField(default=b'JSON', max_length=10, choices=[(b'JSON', b'JSON'), (b'HTML', b'HTML')])),
                ('response_status_code', models.IntegerField(default=200, max_length=10, choices=[(100, b'1xx Informational'), (200, b'2xx Success'), (200, b'3xx Redirection'), (200, b'4xx Client Error'), (200, b'5xx Server Error')])),
                ('response_body', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
