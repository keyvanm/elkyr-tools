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
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('due_date', models.DateField()),
                ('state', models.IntegerField(default=0, choices=[(0, b'Not Started'), (1, b'Started'), (2, b'Blocked'), (3, b'Finished')])),
                ('difficulty', models.IntegerField(default=0, choices=[(0, b'Not Started'), (1, b'Started'), (2, b'Blocked'), (3, b'Finished')])),
                ('description', models.TextField()),
                ('assigned_to', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
            ],
            options={
                'ordering': [b'due_date'],
                'verbose_name_plural': b'stories',
            },
            bases=(models.Model,),
        ),
    ]
