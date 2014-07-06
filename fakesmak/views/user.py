from django.contrib.auth.models import User

from elkyrtools.viewsets import OwnerRestrictedViewSet
from fakesmak.serializers import UserSimpleSerializer, UserListSerializer, UserComplexSerializer, \
    UserOwnerOnUsernameSimpleSerializer, UserOwnerOnUsernameComplexSerializer


class UserViewSet(OwnerRestrictedViewSet):
    simple_serializer_class = UserSimpleSerializer
    list_serializer_class = UserListSerializer
    complex_serializer_class = UserComplexSerializer
    owner_simple_serializer_class = UserOwnerOnUsernameSimpleSerializer
    owner_complex_serializer_class = UserOwnerOnUsernameComplexSerializer
    owner_field = 'username'
    lookup_field = 'username'
    queryset = User.objects.all()