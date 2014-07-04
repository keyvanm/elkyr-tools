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
        ('fakesmak', '0002_auto_20140704_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('profile_picture', models.ImageField(upload_to=b'profile_pics')),
                ('bio', models.TextField()),
                ('is_verified_facebook', models.BooleanField()),
                ('is_verified_text', models.BooleanField()),
                ('date_of_birth', models.DateField()),
                ('interests', taggit.managers.TaggableManager(to=taggit.models.Tag, through=taggit.models.TaggedItem, help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
