from rest_framework import serializers

from event import TagListSerializer
from user import SimpleUserSerializer
from fakesmak.models import UserProfile


class SimpleUserProfileSerializer(serializers.HyperlinkedModelSerializer):
    interests = TagListSerializer()
    avatar = serializers.ImageField(read_only=True)
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    is_verified_facebook = serializers.BooleanField(read_only=True)
    is_verified_text = serializers.BooleanField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('url', 'user', 'avatar', 'bio', 'is_verified_facebook', 'is_verified_text',
                  'date_of_birth', 'interests')


class ListUserProfileSerializer(SimpleUserProfileSerializer):
    pass


class ComplexUserProfileSerializer(SimpleUserProfileSerializer):
    user = SimpleUserSerializer()