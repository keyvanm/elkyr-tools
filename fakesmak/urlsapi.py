from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

import views


router = DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'profiles', views.UserProfileViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
