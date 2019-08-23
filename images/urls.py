from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('images', views.ListAllImages)
router.register('comment', views.ListAllComment)
router.register('likes', views.ListAllLikes)

urlpatterns = [
    path('', include(router.urls)),
]