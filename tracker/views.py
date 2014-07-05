from django.contrib.auth.models import User
from rest_framework import permissions

from elkyrtools.viewsets import ReadOnlyListViewViewSet, CreateListViewViewSet

from tracker import permissions as tracker_permissions
from serializers import SimpleProjectSerializer, SimpleStorySerializer, ComplexProjectSerializer, \
    ComplexStorySerializer, ComplexUserSerializer, ListProjectSerializer, ListStorySerializer, SimpleUserSerializer, \
    ListUserSerializer
from models import Project, Story


class ProjectViewSet(CreateListViewViewSet):
    complex_serializer_class = ComplexProjectSerializer
    simple_serializer_class = SimpleProjectSerializer
    list_serializer_class = ListProjectSerializer
    queryset = Project.objects.all()
    permission_classes = (
        permissions.IsAuthenticated, permissions.tracker_permissions.AuthenticatedDevIsManagerOrReadOnly,)


class StoryViewSet(CreateListViewViewSet):
    complex_serializer_class = ComplexStorySerializer
    simple_serializer_class = SimpleStorySerializer
    list_serializer_class = ListStorySerializer
    queryset = Story.objects.all()
    permission_classes = (permissions.IsAuthenticated, tracker_permissions.DevIsAssignedOrManagerOrReadOnly,)


class UserViewSet(ReadOnlyListViewViewSet):
    complex_serializer_class = ComplexUserSerializer
    simple_serializer_class = SimpleUserSerializer
    list_serializer_class = ListUserSerializer
    lookup_field = 'username'
    queryset = User.objects.all()
