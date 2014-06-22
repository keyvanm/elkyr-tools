# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='difficulty',
            field=models.IntegerField(default=0, choices=[(0, b'Trivial'), (1, b'Easy'), (2, b'Difficult'), (3, b'Very difficult')]),
        ),
    ]
