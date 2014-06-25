import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'stories', views.StoryViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)