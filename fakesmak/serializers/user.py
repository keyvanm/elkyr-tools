from rest_framework import serializers
from django.contrib.auth.models import User


class UserSimpleSerializer(serializers.HyperlinkedModelSerializer):
    # TODO: nobody except the user him/herself should see another person's email
    profile = serializers.PrimaryKeyRelatedField()
    username = serializers.Field()
    profile = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'email', 'profile')
        lookup_field = 'username'


class UserListSerializer(UserSimpleSerializer):
    pass


class UserComplexSerializer(UserSimpleSerializer):
    from fakesmak.serializers.userprofile import UserProfileSimpleSerializer
    from fakesmak.serializers.event import EventNestedInUserSerializer
    profile = UserProfileSimpleSerializer(read_only=True)
    # TODO: Just the user itself should see the attended_events
    attended_events = EventNestedInUserSerializer(many=True)
    hosted_events = EventNestedInUserSerializer(many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'email', 'profile', 'attended_events', 'hosted_events')
        lookup_field = 'username'


class UserNestedInEventSerializer(UserSimpleSerializer):
    username = serializers.Field()
    first_name = serializers.Field()
    avatar = serializers.ImageField(source='profile.avatar', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'avatar')
        lookup_field = 'username'
