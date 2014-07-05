from elkyrtools.viewsets import CreateListViewViewSet
from fakesmak.models import UserProfile
from fakesmak.serializers import UserProfileSimpleSerializer, UserProfileListSerializer, UserProfileComplexSerializer


class UserProfileViewSet(CreateListViewViewSet):
    simple_serializer_class = UserProfileSimpleSerializer
    list_serializer_class = UserProfileListSerializer
    complex_serializer_class = UserProfileComplexSerializer
    queryset = UserProfile.objects.all()