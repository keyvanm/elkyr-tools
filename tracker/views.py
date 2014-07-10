from django.contrib.auth.models import User
from rest_framework import permissions, viewsets, renderers
from rest_framework.decorators import link
from rest_framework.response import Response

from elkyrtools.viewsets import SLCGenericAPIViewMixin
from tracker import permissions as tracker_permissions
from serializers import SimpleProjectSerializer, SimpleStorySerializer, ComplexProjectSerializer, \
    ComplexStorySerializer, ComplexUserSerializer, ListProjectSerializer, ListStorySerializer, ListUserSerializer
from models import Project, Story


class ProjectViewSet(viewsets.ModelViewSet, SLCGenericAPIViewMixin):
    complex_serializer_class = ComplexProjectSerializer
    simple_serializer_class = SimpleProjectSerializer
    list_serializer_class = ListProjectSerializer
    queryset = Project.objects.all()
    permission_classes = (
        permissions.IsAuthenticated, tracker_permissions.DevIsManagerOrReadOnly,)


class StoryViewSet(viewsets.ModelViewSet, SLCGenericAPIViewMixin):
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

    @link(renderer_classes=[renderers.StaticHTMLRenderer])
    def description(self, request, *args, **kwargs):
        story = self.get_object()
        link_to_admin = "/admin/tracker/story/%d/" % story.pk
        anchor_tag_link_to_admin = '<a href="%s">Edit</a>' % link_to_admin
        return Response(story.description + "<hr>" + anchor_tag_link_to_admin)


class UserViewSet(viewsets.ReadOnlyModelViewSet, SLCGenericAPIViewMixin):
    complex_serializer_class = ComplexUserSerializer
    list_serializer_class = ListUserSerializer
    lookup_field = 'username'
    queryset = User.objects.all()
