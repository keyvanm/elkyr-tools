from rest_framework import serializers
from rest_framework.exceptions import ParseError


class TagListSerializer(serializers.WritableField):
    def validate(self, value):
        if type(value) is not list:
            raise serializers.ValidationError("expected a list of data for tags")
        return value

    def to_native(self, obj):
        if type(obj) is not list:
            if type(obj) is not unicode:
                return [tag.name for tag in obj.all()]
        return obj