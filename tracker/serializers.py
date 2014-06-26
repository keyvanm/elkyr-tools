from django.contrib.auth.models import User

from rest_framework import serializers
from tracker.models import Project, Story


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username')
        lookup_field = 'username'


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    manager = serializers.SlugRelatedField(read_only=False, slug_field='username')
    contributors = serializers.SlugRelatedField(many=True, read_only=False, slug_field='username')

    class Meta:
        model = Project
        fields = ('url', 'name', 'manager', 'created_at', 'release_date', 'contributors',)


class StorySerializer(serializers.HyperlinkedModelSerializer):
    project = serializers.PrimaryKeyRelatedField(read_only=False)
    assigned_to = serializers.SlugRelatedField(read_only=False, slug_field='username')

    class Meta:
        model = Story
        fields = (
            'url', 'name', 'project', 'created_at', 'due_date', 'state', 'difficulty', 'description', 'assigned_to')


class ProjectNestedSerializer(ProjectSerializer):
    manager = UserSerializer(read_only=False)
    contributors = UserSerializer(many=True, read_only=False)


class StoryNestedSerializer(StorySerializer):
    project = ProjectNestedSerializer(read_only=False)
    assigned_to = UserSerializer(read_only=False)
