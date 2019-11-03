from django.urls import path
from users import views

urlpatterns = [
    path('explore/', views.ExploreUsers.as_view()),  # 모든 이미지
]
