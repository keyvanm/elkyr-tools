from django.contrib.auth.models import User
from rest_framework import serializers
from tracker.models import Project, Story


class SimpleUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username')
        lookup_field = 'username'


class SimpleStorySerializer(serializers.HyperlinkedModelSerializer):
    project = serializers.PrimaryKeyRelatedField(read_only=False)
    assigned_to = serializers.SlugRelatedField(read_only=False, slug_field='username')

    class Meta:
        model = Story
        fields = (
            'url', 'name', 'project', 'created_at', 'due_date', 'state', 'difficulty', 'description', 'assigned_to')


class SimpleProjectSerializer(serializers.HyperlinkedModelSerializer):
    manager = serializers.SlugRelatedField(read_only=False, slug_field='username')
    contributors = serializers.SlugRelatedField(many=True, read_only=False, slug_field='username')
    stories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('url', 'name', 'manager', 'created_at', 'release_date', 'contributors', 'stories')


class ListProjectSerializer(SimpleProjectSerializer):
    pass


class ComplexProjectSerializer(SimpleProjectSerializer):
    manager = SimpleUserSerializer(read_only=False)
    contributors = SimpleUserSerializer(many=True, read_only=False)


class ListUserSerializer(SimpleUserSerializer):
    pass


class ComplexUserSerializer(SimpleUserSerializer):
    stories = SimpleStorySerializer(many=True)
    managed_projects = SimpleProjectSerializer(many=True, read_only=True)
    contributed_projects = SimpleProjectSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'stories', 'managed_projects', 'contributed_projects')
        lookup_field = 'username'


class ListStorySerializer(SimpleStorySerializer):
    pass


class ComplexStorySerializer(SimpleStorySerializer):
    project = ComplexProjectSerializer(read_only=False)
    assigned_to = SimpleUserSerializer(read_only=False)
