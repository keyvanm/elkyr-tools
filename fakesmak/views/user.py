from django.contrib.auth.models import User
from elkyrtools.viewsets import CreateListViewViewSet
from fakesmak.serializers import UserSimpleSerializer, UserListSerializer, UserComplexSerializer


class UserViewSet(CreateListViewViewSet):
    simple_serializer_class = UserSimpleSerializer
    list_serializer_class = UserListSerializer
    complex_serializer_class = UserComplexSerializer
    lookup_field = 'username'
    queryset = User.objects.all()