from rest_framework import serializers
from django.contrib.auth.models import User

from userprofile import SimpleUserProfileSerializer


class SimpleUserSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'profile')
        lookup_field = 'username'
