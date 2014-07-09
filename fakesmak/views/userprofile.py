from rest_framework import viewsets

from elkyrtools.viewsets import SLCGenericAPIViewMixin
from fakesmak.models import UserProfile
from fakesmak.serializers import UserProfileSimpleSerializer, UserProfileListSerializer, UserProfileComplexSerializer


class UserProfileViewSet(viewsets.ModelViewSet, SLCGenericAPIViewMixin):
    simple_serializer_class = UserProfileSimpleSerializer
    list_serializer_class = UserProfileListSerializer
    complex_serializer_class = UserProfileComplexSerializer
    queryset = UserProfile.objects.all()