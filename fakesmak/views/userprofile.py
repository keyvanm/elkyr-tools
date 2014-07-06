from elkyrtools.viewsets import ViewSetMixin
from fakesmak.models import UserProfile
from fakesmak.serializers import UserProfileSimpleSerializer, UserProfileListSerializer, UserProfileComplexSerializer


class UserProfileViewSet(ViewSetMixin):
    simple_serializer_class = UserProfileSimpleSerializer
    list_serializer_class = UserProfileListSerializer
    complex_serializer_class = UserProfileComplexSerializer
    queryset = UserProfile.objects.all()