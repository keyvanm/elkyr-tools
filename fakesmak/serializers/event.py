from rest_framework import serializers

from fakesmak.models import Event


class EventSimpleSerializer(serializers.HyperlinkedModelSerializer):
    from fakesmak.serializers.tag import TagListSerializer

    tags = TagListSerializer()
    host = serializers.SlugRelatedField(read_only=False, slug_field='username')
    # attendees = serializers.SlugRelatedField(many=True, read_only=False, slug_field='username')

    class Meta:
        model = Event
        fields = ("url", "name", "host", "start_time", "end_time", "location_lat", "location_long", "address",
                  "description", "tags", "upvotes", "downvotes")


class EventOwnerOnHostSimpleSerializer(EventSimpleSerializer):
    attendees = serializers.SlugRelatedField(many=True, read_only=False, slug_field='username')

    class Meta:
        model = Event
        fields = ("url", "name", "host", "start_time", "end_time", "location_lat", "location_long", "address",
                  "description", "tags", "attendees", "upvotes", "downvotes")


class EventNestedInUserSerializer(EventSimpleSerializer):
    host_avatar = serializers.ImageField(source='host.profile.avatar', read_only=True)

    class Meta:
        model = Event
        fields = ("url", "name", "location_lat", "location_long", "start_time", "host", "host_avatar",)


class EventListSerializer(EventSimpleSerializer):
    from user import UserNestedInEventSerializer

    host = UserNestedInEventSerializer()

    class Meta:
        model = Event
        fields = ("url", "name", "host", "start_time", "end_time", "location_lat", "location_long", "tags", "upvotes",
                  "downvotes")


class EventComplexSerializer(EventSimpleSerializer):
    from user import UserNestedInEventSerializer

    host = UserNestedInEventSerializer()
    attendees = UserNestedInEventSerializer(many=True)
