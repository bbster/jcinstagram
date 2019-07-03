from django.db import models
from users import models as user_models


class TimeStampedModel(models.Model):    # 게시물 업로드 및 수정 날짜 모델

    created_at = models.DateTimeField(auto_now_add=True) # 생성 날짜
    updated_at = models.DateTimeField(auto_now=True)     # 수정 날짜

    class Meta:    # 필드가 아닌것 정의
        abstract = True


class Image(TimeStampedModel):    # 이미지 관련 모델
        file = models.ImageField()    # 이미지 업로드
        location = models.CharField(max_length=140)    # 위치정보
        caption = models.TextField()    # 설명
        creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)


class Comment(TimeStampedModel):    # 댓글 관련 모델
    message = models.TextField()    # 댓글
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)


class Like(TimeStampedModel):
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
