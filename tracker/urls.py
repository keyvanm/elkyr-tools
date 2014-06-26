import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'stories', views.StoryViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'users/(?P<username>\w+)/managed_projects', views.ManagedProjectsByUserViewSet)
router.register(r'users/(?P<username>\w+)/contributed_projects', views.ContributionsByUserViewSet)
router.register(r'users/(?P<username>\w+)/stories', views.StoriesByUserViewSet)
router.register(r'projects/(?P<project_pk>\d+)/stories', views.StoriesByProjectViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
