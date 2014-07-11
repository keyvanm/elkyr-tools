from rest_framework import serializers


class AbsUrlFileField(serializers.Field):
    def to_native(self, file_object):
        # return '%s%s' % (settings.MEDIA_URL, file_object)
        return self.context['request'].build_absolute_uri(file_object.url)