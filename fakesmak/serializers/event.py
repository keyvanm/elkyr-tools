from rest_framework import serializers

from fakesmak.models import Event
from fakesmak.serializers.tag import TagListSerializer


class SimpleEventSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagListSerializer()
    host = serializers.SlugRelatedField(read_only=False, slug_field='username')
    attendees = serializers.SlugRelatedField(many=True, read_only=False, slug_field='username')

    class Meta:
        model = Event
        fields = ("url", "name", "host", "start_time", "end_time", "location_lat", "location_long", "address",
                  "description", "tags", "attendees", "upvotes", "downvotes")


class LimitedEventSerializer(SimpleEventSerializer):
    host_avatar = serializers.ImageField(source='host.profile.avatar', read_only=True)

    class Meta:
        model = Event
        fields = ("url", "name", "location_lat", "location_long", "start_time", "host", "host_avatar",)


class ListEventSerializer(SimpleEventSerializer):
    from user import LimitedUserSerializer
    host = LimitedUserSerializer()

    class Meta:
        model = Event
        fields = ("url", "name", "host", "start_time", "end_time", "location_lat", "location_long", "tags", "upvotes",
                  "downvotes")


class ComplexEventSerializer(SimpleEventSerializer):
    from user import LimitedUserSerializer
    host = LimitedUserSerializer()
    attendees = LimitedUserSerializer(many=True)
