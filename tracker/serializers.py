from rest_framework import serializers
from tracker.models import Project, Story


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    manager = serializers.PrimaryKeyRelatedField(read_only=False)
    contributors = serializers.PrimaryKeyRelatedField(many=True, read_only=False, required=False)

    class Meta:
        model = Project
        fields = ('url', 'name', 'manager', 'created_at', 'release_date', 'contributors',)


class StorySerializer(serializers.HyperlinkedModelSerializer):
    project = serializers.PrimaryKeyRelatedField(read_only=False)
    assigned_to = serializers.PrimaryKeyRelatedField(read_only=False)

    class Meta:
        model = Story
        fields = ('url', 'name', 'project', 'created_at', 'due_date', 'state', 'difficulty', 'description', 'assigned_to')
