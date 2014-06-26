from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics
from tracker import permissions as tracker_permissions
from serializers import SimpleProjectSerializer, SimpleStorySerializer, ProjectNestedSerializer, StoryNestedSerializer, \
    UserNestedSerializer
from models import Project, Story


class ProjectViewSet(viewsets.ModelViewSet):
    model = Project
    permission_classes = (tracker_permissions.AuthenticatedDevIsManagerOrReadOnly,)

    # TODO: On listing they should use the simple serializer too
    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return ProjectNestedSerializer
        else:
            return SimpleProjectSerializer


class StoryViewSet(viewsets.ModelViewSet):
    model = Story
    permission_classes = (tracker_permissions.AuthenticatedDevIsAssignedOrManagerOrReadOnly,)

    # TODO: On listing they should use the simple serializer too
    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return StoryNestedSerializer
        else:
            return SimpleStorySerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    # TODO: On listing they should use the simple serializer too
    lookup_field = 'username'
    model = User
    serializer_class = UserNestedSerializer


class ManagedProjectsByUserViewSet(viewsets.ModelViewSet):
    model = Project
    serializer_class = SimpleProjectSerializer

    def get_queryset(self):
        username = self.kwargs.get('username', None)
        if username is not None:
            return Project.objects.filter(manager__username=username)
        return []

    # TODO: Make sure post requests automatically set the manager to the user


class ContributionsByUserViewSet(viewsets.ReadOnlyModelViewSet):
    model = Project
    serializer_class = SimpleProjectSerializer

    def get_queryset(self):
        username = self.kwargs.get('username', None)
        if username is not None:
            return Project.objects.filter(contributors__username=username)
        return []


class StoriesByProjectViewSet(viewsets.ModelViewSet):
    model = Story
    serializer_class = SimpleStorySerializer

    def get_queryset(self):
        project_pk = self.kwargs.get('project_pk', None)
        if project_pk is not None:
            return Story.objects.filter(project__pk=project_pk)
        return []

    # TODO: Make sure post requests automatically set the project to the project


class StoriesByUserViewSet(viewsets.ReadOnlyModelViewSet):
    model = Story
    serializer_class = SimpleStorySerializer

    def get_queryset(self):
        username = self.kwargs.get('username', None)
        if username is not None:
            return Story.objects.filter(assigned_to__username=username)
        return []
