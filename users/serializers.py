from rest_framework import serializers
from . import models

#  데이터를 Json 형태로 변환 시켜줌


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'username',
            'name',
            'bio',
            'website',
            'post_count',
            'followers_count',
            'following_count'
        )


class ExploreUserSerializer(serializers.ModelSerializer):  # 유저  프로필이미지, 아이디

    class Meta:
        model = models.User
        fields = (
            'id',
            'profile_image',
            'username',
            'name',
        )
