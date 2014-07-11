from rest_framework import serializers

from fakesmak.fields import AbsUrlFileField
from fakesmak.models import UserProfile


class UserProfileSimpleSerializer(serializers.HyperlinkedModelSerializer):
    from fakesmak.serializers.tag import TagListSerializer

    interests = TagListSerializer()
    avatar = AbsUrlFileField()
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    is_verified_facebook = serializers.BooleanField(read_only=True)
    is_verified_text = serializers.BooleanField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('url', 'user', 'avatar', 'bio', 'is_verified_facebook', 'is_verified_text',
                  'date_of_birth', 'interests')


class UserProfileListSerializer(UserProfileSimpleSerializer):
    pass


class UserProfileComplexSerializer(UserProfileSimpleSerializer):
    from fakesmak.serializers.user import UserSimpleSerializer

    user = UserSimpleSerializer()
