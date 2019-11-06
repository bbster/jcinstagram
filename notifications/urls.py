from django.urls import path
from notifications import views

urlpatterns = [
    path('', views.Notifications.as_view()),  # 모든 유저

]