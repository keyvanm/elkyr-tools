#!/usr/bin/env python

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tracker.settings")
import django
django.setup()

from django.contrib.auth.models import User

if User.objects.count() == 0:
    admin = User.objects.create_user('admin', 'email@example.com', 'password')
    admin.is_superuser = True
    admin.is_staff = True
    admin.save()