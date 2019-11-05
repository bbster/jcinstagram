from django.urls import path
from images import views

urlpatterns = [
    path('allimages/', views.ListAllImages.as_view()),  # 모든 이미지
    path('allcomments/', views.ListAllComments.as_view()),  # 모든 댓글
    path('alllikes/', views.ListAllLikes.as_view()),  # 모든 좋아요
    path('feed/', views.Feed.as_view()),  # 유저관련
    path('<int:image_id>/like/', views.LikeImage.as_view()),  # 이미지 좋아요, 좋아요 삭제
    path('<int:image_id>/unlike/', views.UnLikeImage.as_view()),  # 이미지 좋아요, 좋아요 삭제
    path('<int:image_id>/comment/', views.CommentOnImage.as_view()),  # 이미지 좋아요, 좋아요 삭제
    path('comment/<int:comment_id>/', views.Comment.as_view()),  # 이미지 좋아요, 좋아요 삭제
    path('search/hashtags/', views.SearchHashtags.as_view()),  # 이미지 좋아요, 좋아요 삭제

]
