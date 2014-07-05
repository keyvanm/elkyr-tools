from rest_framework import permissions
from django.contrib.auth.models import User

from elkyrtools.viewsets import CreateListViewViewSet

from serializers import SimpleEventSerializer, SimpleUserProfileSerializer, SimpleUserSerializer, ListEventSerializer, \
    ComplexEventSerializer, ListUserSerializer, ComplexUserSerializer, ListUserProfileSerializer, \
    ComplexUserProfileSerializer
from models import Event, UserProfile


class EventViewSet(CreateListViewViewSet):
    simple_serializer_class = SimpleEventSerializer
    list_serializer_class = ListEventSerializer
    complex_serializer_class = ComplexEventSerializer
    queryset = Event.objects.all()
    permission_classes = (permissions.IsAuthenticated, )

    def post_save(self, *args, **kwargs):
        if 'tags' in self.request.DATA:
            saved_event = Event.objects.get(pk=self.object.pk)
            saved_event.tags.set(*self.request.DATA['tags'])
        return super(EventViewSet, self).post_save(*args, **kwargs)


class UserViewSet(CreateListViewViewSet):
    simple_serializer_class = SimpleUserSerializer
    list_serializer_class = ListUserSerializer
    complex_serializer_class = ComplexUserSerializer
    lookup_field = 'username'
    queryset = User.objects.all()


class UserProfileViewSet(CreateListViewViewSet):
    simple_serializer_class = SimpleUserProfileSerializer
    list_serializer_class = ListUserProfileSerializer
    complex_serializer_class = ComplexUserProfileSerializer
    queryset = UserProfile.objects.all()
