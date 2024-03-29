# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0002_auto_20140621_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('manager', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('release_date', models.DateField()),
                ('contributers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='story',
            name='project',
            field=models.ForeignKey(to='tracker.Project', default=1, to_field='id'),
            preserve_default=False,
        ),
    ]
