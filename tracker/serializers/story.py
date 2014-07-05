from rest_framework import serializers

from tracker.models import Story


class SimpleStorySerializer(serializers.HyperlinkedModelSerializer):
    project = serializers.PrimaryKeyRelatedField(read_only=False)
    assigned_to = serializers.SlugRelatedField(read_only=False, slug_field='username')

    class Meta:
        model = Story
        fields = (
            'url', 'name', 'project', 'created_at', 'due_date', 'state', 'difficulty', 'description', 'assigned_to')


class ListStorySerializer(SimpleStorySerializer):
    pass


class ComplexStorySerializer(SimpleStorySerializer):
    from user import SimpleUserSerializer
    from project import ComplexProjectSerializer

    project = ComplexProjectSerializer(read_only=False)
    assigned_to = SimpleUserSerializer(read_only=False)
