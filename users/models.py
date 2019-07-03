from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    GENDER_CHOICES = (      # 성별 선택
        ('여자', '여자'),
        ('남자', '남자'),

    )
    name = models.CharField(max_length=150, blank=True)    # 이름 값
    website = models.URLField(blank=True)                  # 웹 사이트 입력
    bio = models.TextField(blank=True)                     #
    phone = models.CharField(max_length=50, blank=True, null=True)    # 전화번호
    gender = models.CharField(max_length=20, blank=True, choices=GENDER_CHOICES, null=True)    # 성별선택
    followers = models.ManyToManyField("self")
    following = models.ManyToManyField("self")

    def __str__(self):
        return self.username
