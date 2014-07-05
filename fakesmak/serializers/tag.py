from rest_framework import serializers
from rest_framework.exceptions import ParseError


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