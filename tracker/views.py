from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from serializers import ProjectSerializer, StorySerializer, UserSerializer, ProjectNestedSerializer, \
    StoryNestedSerializer
from models import Project, Story


class ProjectViewSet(viewsets.ModelViewSet):
    model = Project

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return ProjectNestedSerializer
        else:
            return ProjectSerializer


class StoryViewSet(viewsets.ModelViewSet):
    model = Story

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return StoryNestedSerializer
        else:
            return StorySerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'username'
    model = User
    serializer_class = UserSerializer
