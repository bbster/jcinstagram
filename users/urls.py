from django.urls import path
from users import views

urlpatterns = [
    path('explore/', views.ExplorerUsers.as_view()),  # 모든 이미지
]
