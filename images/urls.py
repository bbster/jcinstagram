from django.urls import include, path
from images import views

urlpatterns = [
    path('images/', views.ListAllImages.as_view()),
    path('comments/', views.ListAllComments.as_view()),
    path('likes/', views.ListAllLikes.as_view()),
    path('<int:image_id>/like/', views.LikeImage.as_view()),
    path('feed/', views.Feed.as_view()),
]
