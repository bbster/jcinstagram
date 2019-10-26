from rest_framework import serializers
from . import models


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    # comment, like 직렬화
    comments = CommentSerializer(many=True)
    likes = LikeSerializer(many=True)

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'creator',
            'comments',
            'likes',
        )
