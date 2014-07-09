from rest_framework import permissions, viewsets

from elkyrtools.viewsets import SLCGenericAPIViewMixin
from fakesmak.models import Event
from fakesmak.serializers import EventSimpleSerializer, EventListSerializer, EventComplexSerializer


class EventViewSet(viewsets.ModelViewSet, SLCGenericAPIViewMixin):
    simple_serializer_class = EventSimpleSerializer
    list_serializer_class = EventListSerializer
    complex_serializer_class = EventComplexSerializer
    queryset = Event.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    owner = 'host'

    def post_save(self, *args, **kwargs):
        if 'tags' in self.request.DATA:
            saved_event = Event.objects.get(pk=self.object.pk)
            saved_event.tags.set(*self.request.DATA['tags'])
        return super(EventViewSet, self).post_save(*args, **kwargs)