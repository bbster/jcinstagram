from rest_framework import serializers
from . import models
from users import models as user_models

#  데이터를 Json 형태로 변환 시켜줌


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'like_count',
            'comment_count',
        )


class FeedUserSerializer(serializers.ModelSerializer):  # 유저  프로필이미지, 아이디

    class Meta:
        model = user_models.User
        fields = (
            'profile_image',
            'username',
        )


class CommentSerializer(serializers.ModelSerializer):  # 게시물  아이디, 댓글

    creator = FeedUserSerializer(read_only=True)

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'creator',
            'message',
        )


class LikeSerializer(serializers.ModelSerializer):  # 좋아요  아이디

    creator = FeedUserSerializer()

    class Meta:
        model = models.Like
        fields = (
            'creator',
        )


class ImageSerializer(serializers.ModelSerializer):  # 이미지  아이디, 이미지파일, 위치, 캡션, 게시글, 좋아요횟수
    # comment, like 직렬화
    comments = CommentSerializer(many=True)
    creator = FeedUserSerializer()

    class Meta:
        model = models.Image
        fields = (
            'id',
            'creator',
            'file',
            'location',
            'caption',
            'comments',
            'like_count',
        )
