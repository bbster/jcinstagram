from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register('images', views.ListAllImages)
# router.register('comments', views.ListAllComment)
# router.register('likes', views.ListAllLikes)
router.register('feed', views.Feed) # 인스타그램 게시물

urlpatterns = [
    # path('feed', views.Feed.as_view(), name='feed'),
    path('', include(router.urls)),
]