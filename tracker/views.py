from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics
from tracker import permissions as tracker_permissions
from serializers import SimpleProjectSerializer, SimpleStorySerializer, ProjectNestedSerializer, StoryNestedSerializer, \
    UserNestedSerializer
from models import Project, Story


class ProjectViewSet(viewsets.ModelViewSet):
    model = Project
    permission_classes = (tracker_permissions.AuthenticatedDevIsManagerOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return ProjectNestedSerializer
        else:
            return SimpleProjectSerializer


class StoryViewSet(viewsets.ModelViewSet):
    model = Story
    permission_classes = (tracker_permissions.AuthenticatedDevIsAssignedOrManagerOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return StoryNestedSerializer
        else:
            return SimpleStorySerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'username'
    model = User
    serializer_class = UserNestedSerializer


class ManagedProjectsByUserList(generics.ListCreateAPIView):
    model = Project
    serializer_class = SimpleProjectSerializer

    def get_queryset(self):
        username = self.kwargs.get('username', None)
        if username is not None:
            return Project.objects.filter(manager__username=username)
        return []

    # TODO: Make sure post requests automatically set the manager to the user


class ContributionsByUserList(generics.ListAPIView):
    model = Project
    serializer_class = SimpleProjectSerializer

    def get_queryset(self):
        username = self.kwargs.get('username', None)
        if username is not None:
            return Project.objects.filter(contributors__username=username)
        return []


class StoriesByProjectList(generics.ListCreateAPIView):
    model = Story
    serializer_class = SimpleStorySerializer

    def get_queryset(self):
        project_pk = self.kwargs.get('project_pk', None)
        if project_pk is not None:
            return Story.objects.filter(project__pk=project_pk)
        return []