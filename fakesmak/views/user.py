from django.contrib.auth.models import User
from rest_framework import viewsets

from elkyrtools.viewsets import SLCGenericAPIViewMixin
from fakesmak.serializers import UserSimpleSerializer, UserListSerializer, UserComplexSerializer


class UserViewSet(viewsets.ModelViewSet, SLCGenericAPIViewMixin):
    simple_serializer_class = UserSimpleSerializer
    list_serializer_class = UserListSerializer
    complex_serializer_class = UserComplexSerializer
    lookup_field = 'username'
    queryset = User.objects.all()

    owner = 'self'
    private_to_owner_fields = ('email', 'attended_events',)
