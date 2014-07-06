from rest_framework import viewsets, permissions
from django.core import exceptions


class ReadOnlyViewSetMixin(viewsets.ReadOnlyModelViewSet):
    """
    A view set that supports 2 different kinds of serialization for listing and viewing objects
    2 fields need to be defined on the viewset that subclasses it
    complex_serializer_class
    list_serializer_class
    """

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
        return self.limit_serializer_class_if_needed(self.complex_serializer_class)

    def list(self, request, **kwargs):
        # Override get_serializer_class method to return the List Serializer
        self.get_serializer_class = lambda: self.limit_serializer_class_if_needed(self.list_serializer_class)
        return super(viewsets.ReadOnlyModelViewSet, self).list(self, request)


class ViewSetMixin(viewsets.ModelViewSet, ReadOnlyViewSetMixin):
    """
    Same as ReadOnlyViewSetMixin but with the addition of creation of objects
    In addition to the super class's fields it needs another field defined:
    simple_serializer_class
    """

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return self.limit_serializer_class_if_needed(self.complex_serializer_class)
        else:
            return self.limit_serializer_class_if_needed(self.simple_serializer_class)

