# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('host', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('location_lat', models.DecimalField(max_digits=9, decimal_places=6)),
                ('location_long', models.DecimalField(max_digits=9, decimal_places=6)),
                ('address', models.TextField()),
                ('description', models.TextField()),
                ('upvotes', models.PositiveIntegerField()),
                ('downvotes', models.PositiveIntegerField()),
                ('attendees', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(to=taggit.models.Tag, through=taggit.models.TaggedItem, help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
