from rest_framework import serializers
from django.contrib.auth.models import User


class SimpleUserSerializer(serializers.HyperlinkedModelSerializer):
    # TODO: nobody except the user him/herself should see another person's email
    profile = serializers.PrimaryKeyRelatedField()
    username = serializers.Field()
    profile = serializers.PrimaryKeyRelatedField(read_only=True)

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
    from userprofile import SimpleUserProfileSerializer
    from event import LimitedEventSerializer
    profile = SimpleUserProfileSerializer(read_only=True)
    # TODO: Just the user itself should see the attended_events
    attended_events = LimitedEventSerializer(many=True)
    hosted_events = LimitedEventSerializer(many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'email', 'profile', 'attended_events', 'hosted_events')
        lookup_field = 'username'