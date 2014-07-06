from rest_framework import serializers
from django.contrib.auth.models import User


class UserSimpleSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.Field()
    profile = serializers.PrimaryKeyRelatedField(read_only=True)
    hosted_events = serializers.PrimaryKeyRelatedField(many=True)
    attended_events = serializers.PrimaryKeyRelatedField(many=True)


    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'profile', 'hosted_events', 'email', 'attended_events')
        lookup_field = 'username'


class UserListSerializer(UserSimpleSerializer):
    pass


class UserComplexSerializer(UserSimpleSerializer):
    from fakesmak.serializers.userprofile import UserProfileSimpleSerializer
    from fakesmak.serializers.event import EventNestedInUserSerializer

    attended_events = EventNestedInUserSerializer(many=True)
    profile = UserProfileSimpleSerializer(read_only=True)
    hosted_events = EventNestedInUserSerializer(many=True)


class UserNestedInEventSerializer(UserSimpleSerializer):
    username = serializers.Field()
    first_name = serializers.Field()
    avatar = serializers.ImageField(source='profile.avatar', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'avatar')
        lookup_field = 'username'
