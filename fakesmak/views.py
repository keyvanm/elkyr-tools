from rest_framework import permissions
from django.contrib.auth.models import User

from elkyrtools.viewsets import CreateListViewViewSet

from serializers import EventSimpleSerializer, UserProfileSimpleSerializer, UserSimpleSerializer, EventListSerializer, \
    EventComplexSerializer, UserListSerializer, UserComplexSerializer, UserProfileListSerializer, \
    UserProfileComplexSerializer
from models import Event, UserProfile


class EventViewSet(CreateListViewViewSet):
    simple_serializer_class = EventSimpleSerializer
    list_serializer_class = EventListSerializer
    complex_serializer_class = EventComplexSerializer
    queryset = Event.objects.all()
    permission_classes = (permissions.IsAuthenticated, )

    def post_save(self, *args, **kwargs):
        if 'tags' in self.request.DATA:
            saved_event = Event.objects.get(pk=self.object.pk)
            saved_event.tags.set(*self.request.DATA['tags'])
        return super(EventViewSet, self).post_save(*args, **kwargs)


class UserViewSet(CreateListViewViewSet):
    simple_serializer_class = UserSimpleSerializer
    list_serializer_class = UserListSerializer
    complex_serializer_class = UserComplexSerializer
    lookup_field = 'username'
    queryset = User.objects.all()


class UserProfileViewSet(CreateListViewViewSet):
    simple_serializer_class = UserProfileSimpleSerializer
    list_serializer_class = UserProfileListSerializer
    complex_serializer_class = UserProfileComplexSerializer
    queryset = UserProfile.objects.all()
