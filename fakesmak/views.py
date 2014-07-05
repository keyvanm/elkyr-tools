from rest_framework import permissions
from django.contrib.auth.models import User

from elkyrtools.viewsets import CreateListViewViewSet

from serializers import SimpleEventSerializer, SimpleUserProfileSerializer, SimpleUserSerializer
from models import Event, UserProfile


class EventViewSet(CreateListViewViewSet):
    complex_serializer_class = SimpleEventSerializer
    simple_serializer_class = SimpleEventSerializer
    list_serializer_class = SimpleEventSerializer
    queryset = Event.objects.all()
    permission_classes = (permissions.IsAuthenticated, )

    def post_save(self, *args, **kwargs):
        if 'tags' in self.request.DATA:
            saved_event = Event.objects.get(pk=self.object.pk)
            saved_event.tags.set(*self.request.DATA['tags'])
        return super(EventViewSet, self).post_save(*args, **kwargs)


class UserViewSet(CreateListViewViewSet):
    complex_serializer_class = SimpleUserSerializer
    simple_serializer_class = SimpleUserSerializer
    list_serializer_class = SimpleUserSerializer
    lookup_field = 'username'
    queryset = User.objects.all()


class UserProfileViewSet(CreateListViewViewSet):
    complex_serializer_class = SimpleUserProfileSerializer
    simple_serializer_class = SimpleUserProfileSerializer
    list_serializer_class = SimpleUserProfileSerializer
    queryset = UserProfile.objects.all()
