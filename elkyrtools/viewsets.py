from rest_framework import viewsets, permissions
from django.core import exceptions


def _is_owner(obj):
    try:
        if obj.owner_field is not None:
            return obj.request.user.username == obj.get_object_or_none().__getattribute__(obj.owner_field).username
        return obj.request.user.username == obj.get_object_or_none().username
    except exceptions.ImproperlyConfigured:
        return False


class ReadOnlyViewSetMixin(viewsets.ReadOnlyModelViewSet):
    """
    A view set that supports 2 different kinds of serialization for listing and viewing objects
    2 fields need to be defined on the viewset that subclasses it
    complex_serializer_class
    list_serializer_class
    """

    def get_serializer_class(self):
        return self.complex_serializer_class

    def list(self, request, **kwargs):
        # Override get_serializer_class method to return the List Serializer
        self.get_serializer_class = lambda: self.list_serializer_class
        return super(viewsets.ReadOnlyModelViewSet, self).list(self, request)


class OwnerRestrictedReadOnlyViewSetMixin(ReadOnlyViewSetMixin):
    """
    If a field needs restriction from unauthorized users, use this ViewSet
    2 new fields:
    owner_field
    owner_complex_serializer_class
    """

    def get_serializer_class(self):
        if _is_owner(self):
            return self.owner_complex_serializer_class
        return self.complex_serializer_class


class ViewSetMixin(viewsets.ModelViewSet, ReadOnlyViewSetMixin):
    """
    Same as ReadOnlyViewSetMixin but with the addition of creation of objects
    In addition to the super class's fields it needs another field defined:
    simple_serializer_class
    """

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return self.complex_serializer_class
        else:
            return self.simple_serializer_class


class OwnerRestrictedViewSet(ViewSetMixin):
    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            if _is_owner(self):
                return self.owner_complex_serializer_class
            return self.complex_serializer_class
        else:
            if _is_owner(self):
                return self.owner_simple_serializer_class
            return self.simple_serializer_class
