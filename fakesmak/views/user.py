from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from elkyrtools.viewsets import SLCGenericAPIViewMixin, RestrictNonOwnerViewMixin
from fakesmak.serializers import UserSimpleSerializer, UserListSerializer, UserComplexSerializer
from fakesmak.permissions import IsUserItself, IsUserItselfOrReadOnly


class UserViewSet(RestrictNonOwnerViewMixin, SLCGenericAPIViewMixin, viewsets.ModelViewSet):
    lookup_field = 'username'
    model = User
    queryset = User.objects.filter(is_active=True)
    permission_classes = (permissions.IsAuthenticated, IsUserItselfOrReadOnly)

    simple_serializer_class = UserSimpleSerializer
    list_serializer_class = UserListSerializer
    complex_serializer_class = UserComplexSerializer

    owner_permission_class = IsUserItself
    private_to_owner_fields = ('email', 'attended_events',)
