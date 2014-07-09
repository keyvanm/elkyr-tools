from rest_framework import generics, permissions
from django.core import exceptions


def assert_field_exists(obj, field):
    error_message = "'%s' should include a '{0}' attribute" % obj.__class__.__name__
    assert getattr(obj, field, None) is not None, error_message.format(field)


class SLCGenericAPIViewMixin(generics.GenericAPIView):
    """
    A view that supports 2 different kinds of serialization for listing and viewing objects
    2 fields need to be defined on the view that subclasses it
    complex_serializer_class
    list_serializer_class
    If the subclass also needs write permissions, it needs to define
    simple_serializer_class
    """
    simple_serializer_class = None
    list_serializer_class = None
    complex_serializer_class = None

    private_to_owner_fields = None
    owner = None

    def is_requester_the_owner(self):
        """
        Check if the user doing the request is the owner of the object or not
        """
        # TODO: Still feels a bit hacky, feel free to find a better solution later
        try:
            if self.owner != 'self':
                return self.request.user.username == self.get_object_or_none().__getattribute__(self.owner).username
            return self.request.user.username == self.get_object_or_none().username
        except (exceptions.ImproperlyConfigured, AttributeError):
            return False

    def limit_serializer_class_if_needed(self, serializer_class):
        """
        If there are private fields that only the owner should have access to, remove them from the serializer
        """
        if self.private_to_owner_fields is None or self.is_requester_the_owner():
            return serializer_class
        else:
            current_fields = serializer_class.Meta.fields
            limited_fields = tuple(set(current_fields) - set(self.private_to_owner_fields))
            print limited_fields
            serializer_class.Meta.fields = limited_fields
            return serializer_class

    def get_serializer_class(self):
        if getattr(self, 'object', None) is not None:
            if self.request.method in permissions.SAFE_METHODS:
                assert_field_exists(self, "complex_serializer_class")
                return self.limit_serializer_class_if_needed(self.complex_serializer_class)
            else:
                assert_field_exists(self, 'simple_serializer_class')
                return self.limit_serializer_class_if_needed(self.simple_serializer_class)
        else:
            if self.request.method in permissions.SAFE_METHODS:
                assert_field_exists(self, 'list_serializer_class')
                return self.limit_serializer_class_if_needed(self.list_serializer_class)
            else:
                assert_field_exists(self, 'simple_serializer_class')
                return self.limit_serializer_class_if_needed(self.simple_serializer_class)
