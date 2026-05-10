from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import *

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls))
]
