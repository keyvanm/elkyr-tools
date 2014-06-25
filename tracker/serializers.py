from rest_framework import serializers
from tracker.models import Project, Story


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    manager = serializers.RelatedField()
    contributors = serializers.RelatedField(many=True)

    class Meta:
        model = Project
        fields = ('url', 'name', 'manager',
                  'created_at', 'release_date', 'contributors',)
