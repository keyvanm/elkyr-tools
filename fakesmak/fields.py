from rest_framework import serializers


class AbsUrlFileField(serializers.Field):
    def to_native(self, file_object):
        try:
            return self.context['request'].build_absolute_uri(file_object.url)
        except ValueError:
            return ""
