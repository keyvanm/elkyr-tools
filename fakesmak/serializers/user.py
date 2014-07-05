from rest_framework import serializers
from django.contrib.auth.models import User


class SimpleUserSerializer(serializers.HyperlinkedModelSerializer):
    # nobody except the user him/herself should see another person's email
    profile = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'email', 'profile')
        lookup_field = 'username'


class LimitedUserSerializer(SimpleUserSerializer):
    username = serializers.Field()
    first_name = serializers.Field()
    avatar = serializers.ImageField(source='profile.avatar', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'avatar')
        lookup_field = 'username'


class ListUserSerializer(SimpleUserSerializer):
    pass


class ComplexUserSerializer(SimpleUserSerializer):
    pass
