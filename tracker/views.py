from django.contrib.auth.models import User
from rest_framework import viewsets
from serializers import ProjectSerializer
from models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    model = Project
