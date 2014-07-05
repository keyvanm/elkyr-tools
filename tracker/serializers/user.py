from django.contrib.auth.models import User
from rest_framework import serializers


class SimpleUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username')
        lookup_field = 'username'


class ListUserSerializer(SimpleUserSerializer):
    pass


class ComplexUserSerializer(SimpleUserSerializer):
    from story import SimpleStorySerializer
    from project import SimpleProjectSerializer

    stories = SimpleStorySerializer(many=True)
    managed_projects = SimpleProjectSerializer(many=True, read_only=True)
    contributed_projects = SimpleProjectSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'stories', 'managed_projects', 'contributed_projects')
        lookup_field = 'username'
