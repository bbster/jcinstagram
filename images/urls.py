from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('images', views.ListAllImages)
router.register('comments', views.ListAllComment)
router.register('likes', views.ListAllLikes)
router.register('feed', views.Feed)

urlpatterns = [
    path('', include(router.urls)),
]