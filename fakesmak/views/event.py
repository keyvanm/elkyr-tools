from django.utils import timezone

from django.db.models import F

from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from fakesmak.permissions import IsHostOrReadOnly

from elkyrtools.viewsets import SLCGenericAPIViewMixin
from fakesmak.models import Event
from fakesmak.serializers import EventSimpleSerializer, EventListSerializer, EventComplexSerializer


class EventViewSet(viewsets.ModelViewSet, SLCGenericAPIViewMixin):
    simple_serializer_class = EventSimpleSerializer
    list_serializer_class = EventListSerializer
    complex_serializer_class = EventComplexSerializer
    queryset = Event.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsHostOrReadOnly,)

    @action(permission_classes=[permissions.IsAuthenticated])
    def add_yourself_to_event(self, request, pk=None):
        event = self.get_object()
        if not event.is_user_an_attendee(request.user):
            event.attendees.add(request.user)
            return Response({'status': 'user %s added to event %s' % (request.user, event)})
        else:
            return Response({'error': 'user %s is already an attendee of event %s' % (request.user, event)},
                            status=status.HTTP_412_PRECONDITION_FAILED)

    @action(permission_classes=[permissions.IsAuthenticated])
    def remove_yourself_from_event(self, request, pk=None):
        event = self.get_object()
        if event.is_user_an_attendee(request.user):
            event.attendees.remove(request.user)
            return Response({'status': 'user %s removed from event %s' % (request.user, event)})
        else:
            return Response({'error': 'user %s is not an attendee of event %s' % (request.user, event)},
                            status=status.HTTP_412_PRECONDITION_FAILED)

    @action(permission_classes=[permissions.IsAuthenticated])
    def upvote(self, request, pk=None):
        event = self.get_object()
        if timezone.now() >= event.start_time and event.is_user_an_attendee(request.user):
            event.upvotes = F('upvotes') + 1
            event.save(update_fields=['upvotes'])
            return Response({'status': 'user %s upvoted event %s' % (request.user, event)})
        else:
            # TODO: Consider making these two errors separate
            return Response(
                {'error': 'Event %s has not started yet or user %s was not an attendee' % (event, request.user)},
                status=status.HTTP_412_PRECONDITION_FAILED)

    @action(permission_classes=[permissions.IsAuthenticated])
    def downvote(self, request, pk=None):
        event = self.get_object()
        if timezone.now() >= event.start_time and event.is_user_an_attendee(request.user):
            event.upvotes = F('downvotes') + 1
            event.save(update_fields=['downvotes'])
            return Response({'status': 'user %s downvoted event %s' % (request.user, event)})
        else:
            return Response(
                {'error': 'Event %s has not started yet or user %s was not an attendee' % (event, request.user)},
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