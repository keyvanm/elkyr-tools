from rest_framework import serializers

from fakesmak.models import Event


class EventSimpleSerializer(serializers.HyperlinkedModelSerializer):
    from fakesmak.serializers.tag import TagListSerializer

    tags = TagListSerializer()
    # TODO: Host is being readonly here, but I feel like it should be changeable only by the host itself
    host = serializers.SlugRelatedField(slug_field='username', read_only=True)
    attendees = serializers.SlugRelatedField(many=True, slug_field='username', read_only=True)

    class Meta:
        model = Event
        fields = ("url", "id", "name", "host", "start_time", "end_time", "location_lat", "location_long", "address",
                  "description", "tags", "upvotes", "downvotes", "attendees",)
        read_only_fields = ("upvotes", "downvotes",)


class EventNestedInUserSerializer(EventSimpleSerializer):
    host_avatar = serializers.ImageField(source='host.profile.avatar', read_only=True)

    class Meta:
        model = Event
        fields = ("url", "name", "location_lat", "location_long", "start_time", "host", "host_avatar",)


class EventListSerializer(EventSimpleSerializer):
    from user import UserNestedInEventSerializer

    host = UserNestedInEventSerializer(read_only=True)

    class Meta:
        model = Event
        fields = (
            "url", "id", "name", "host", "start_time", "end_time", "location_lat", "location_long", "tags", "upvotes",
            "downvotes")


class EventComplexSerializer(EventSimpleSerializer):
    from user import UserNestedInEventSerializer

    host = UserNestedInEventSerializer(read_only=True)
    attendees = UserNestedInEventSerializer(many=True)
