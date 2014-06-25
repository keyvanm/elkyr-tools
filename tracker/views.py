from django.contrib.auth.models import User
from rest_framework import viewsets
from serializers import ProjectSerializer, StorySerializer
from models import Project, Story


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    model = Project


class StoryViewSet(viewsets.ModelViewSet):
    serializer_class = StorySerializer
    model = Story
