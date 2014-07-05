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
        permissions.IsAuthenticated, tracker_permissions.DevIsManagerOrReadOnly,)


class StoryViewSet(CreateListViewViewSet):
    complex_serializer_class = ComplexStorySerializer
    simple_serializer_class = SimpleStorySerializer
    list_serializer_class = ListStorySerializer
    model = Story
    permission_classes = (permissions.IsAuthenticated, tracker_permissions.DevIsAssignedOrManagerOrReadOnly,)
    filter_fields = ('name',)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `project` query parameter in the URL.
        """
        queryset = Story.objects.all()
        project_name = self.request.QUERY_PARAMS.get('project', None)
        if project_name is not None:
            queryset = queryset.filter(project__name=project_name)
        return queryset


class UserViewSet(ReadOnlyListViewViewSet):
    complex_serializer_class = ComplexUserSerializer
    simple_serializer_class = SimpleUserSerializer
    list_serializer_class = ListUserSerializer
    lookup_field = 'username'
    queryset = User.objects.all()
