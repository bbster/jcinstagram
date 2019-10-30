from rest_framework import serializers
from . import models
from users import models as user_models


class FeedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_models.User
        fields = (
            'username',
            'profile_image',
        )


class CommentSerializer(serializers.ModelSerializer):

    creator = FeedUserSerializer()

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator',
        )


class LikeSerializer(serializers.ModelSerializer):

    creator = FeedUserSerializer()

    class Meta:
        model = models.Like
        fields = (
            'creator',
        )


class ImageSerializer(serializers.ModelSerializer):
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
