from django.db import models
from users import models as user_models


class TimeStampedModel(models.Model):    # 게시물 업로드 및 수정 날짜 모델

    created_at = models.DateTimeField(auto_now_add=True)  # 생성 날짜
    updated_at = models.DateTimeField(auto_now=True)     # 수정 날짜

    class Meta:    # 필드가 아닌것 정의
        abstract = True


class Image(TimeStampedModel):  # 이미지 관련 모델

    file = models.ImageField()    # 이미지 업로드
    location = models.CharField(max_length=140)    # 위치정보
    caption = models.TextField()    # 설명
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True, related_name='images')

    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)

    class Meta:
        ordering = ['-created_at']


class Comment(TimeStampedModel):    # 댓글 관련 모델

    message = models.TextField()    # 댓글

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)

    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, related_name='comments')


class Like(TimeStampedModel):  # 좋아요

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)

    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, related_name='likes')

    # creator username, image caption 반환
    def __str__(self):
        return '{} - {}'.format(self.creator.username,
                                self.image.caption)
