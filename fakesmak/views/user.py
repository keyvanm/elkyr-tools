from django.contrib.auth.models import User
from rest_framework import viewsets

from elkyrtools.viewsets import SLCGenericAPIViewMixin, RestrictNonOwnerViewMixin
from fakesmak.serializers import UserSimpleSerializer, UserListSerializer, UserComplexSerializer


class UserViewSet(RestrictNonOwnerViewMixin, SLCGenericAPIViewMixin, viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()

    simple_serializer_class = UserSimpleSerializer
    list_serializer_class = UserListSerializer
    complex_serializer_class = UserComplexSerializer

    owner = 'self'
    private_to_owner_fields = ('email', 'attended_events',)
