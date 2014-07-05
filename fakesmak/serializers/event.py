from rest_framework import serializers

from fakesmak.models import Event
from rest_framework.exceptions import ParseError
from taggit.forms import TagWidget


class TagListSerializer(serializers.WritableField):
    def from_native(self, data):
        if type(data) is not list:
            raise ParseError("expected a list of data")
        return data

    def to_native(self, obj):
        if type(obj) is not list:
            if type(obj) is not unicode:
                return [tag.name for tag in obj.all()]
        return obj


class SimpleEventSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagListSerializer()
    host = serializers.SlugRelatedField(read_only=False, slug_field='username')
    attendees = serializers.SlugRelatedField(many=True, read_only=False, slug_field='username')

    class Meta:
        model = Event
        fields = ("url", "name", "host", "start_time", "end_time", "location_lat", "location_long", "address",
                  "description", "tags", "attendees", "upvotes", "downvotes")
