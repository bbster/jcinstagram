from django.urls import include, path
from images import views

urlpatterns = [
    path('allimages/', views.ListAllImage.as_view()),
    path('allcomments/', views.ListAllComment.as_view()),
    path('alllikes/', views.ListAllLike.as_view()),
]
