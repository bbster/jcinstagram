from django.urls import path
from users import views

urlpatterns = [
    path('listuser/', views.ListUsers.as_view()),  # 모든 유저
    path('<int:user_id>/follow/', views.FollowUser.as_view()),  # 팔로우
    path('<int:user_id>/unfollow/', views.UnFollowUser.as_view()),  # 언팔로우
    path('<username>/', views.UserProfile.as_view()),  # 프로필 뷰
    path('<username>/userfollowers', views.UserFollowers.as_view()),  # 팔로우 유저리스트
    path('<username>/userfollowing', views.UserFollowing.as_view()),  # 팔로잉 유저리스트
]
