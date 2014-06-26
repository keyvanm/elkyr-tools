import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'stories', views.StoryViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^users/(?P<username>\w+)/managed_projects/$', views.ManagedProjectsByUserList.as_view()),
    url(r'^users/(?P<username>\w+)/contributed_projects/$', views.ContributionsByUserList.as_view()),
    url(r'^projects/(?P<project_pk>\d+)/stories/$', views.StoriesByProjectList.as_view()),
)