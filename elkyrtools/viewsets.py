from rest_framework import viewsets, permissions


class ReadOnlyListViewViewSet(viewsets.ReadOnlyModelViewSet):
    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return self.complex_serializer_class
        else:
            return self.simple_serializer_class

    def list(self, request, **kwargs):
        # Override get_serializer_class method to return the List Serializer
        self.get_serializer_class = lambda: self.list_serializer_class
        return super(viewsets.ReadOnlyModelViewSet, self).list(self, request)


class CreateListViewViewSet(viewsets.ModelViewSet, ReadOnlyListViewViewSet):
    pass
