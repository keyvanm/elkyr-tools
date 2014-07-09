from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action()
    def add_yourself_to_event(self, request, pk=None):
        event = self.get_object()
        event.attendees.add(request.user)
        return Response({'status': 'user %s added to event %s' % (request.user, event)})

    @action()
    def remove_yourself_from_event(self, request, pk=None):
        event = self.get_object()
        if event.attendees.filter(username=request.user):
            event.attendees.remove(request.user)
            return Response({'status': 'user %s removed from event %s' % (request.user, event)})
        else:
            return Response({'error': 'user %s is not an attendee of event %s' % (request.user, event)},
                            status=status.HTTP_412_PRECONDITION_FAILED)

    def pre_save(self, event):
        """
        Set the event's host, based on the incoming request.
        """
        event.host = self.request.user

    def post_save(self, *args, **kwargs):
        """
        Adds the event's host as one of the attendees and saves the tags sent with the request
        """
        saved_event = Event.objects.get(pk=self.object.pk)
        saved_event.attendees.add(saved_event.host)
        if 'tags' in self.request.DATA:
            saved_event.tags.set(*self.request.DATA['tags'])
        return super(EventViewSet, self).post_save(*args, **kwargs)