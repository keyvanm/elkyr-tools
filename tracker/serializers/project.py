from rest_framework import serializers

from tracker.models import Project


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
    from user import SimpleUserSerializer

    manager = SimpleUserSerializer(read_only=False)
    contributors = SimpleUserSerializer(many=True, read_only=False)
