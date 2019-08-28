from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from images.serializers import ImageSerializer, CommentSerializer, LikeSerializer
from .models import Image, Comment, Like
from . import serializers


# class ListAllImages(viewsets.ModelViewSet):
#
#     serializer_class = ImageSerializer
#     queryset = Image.objects.all()
#
#     # @action(detail=True, methods=['get'])
#     def get(self, request, format=None):
#         all_images =  Image.objects.all() # 모든 이미지 출력
#         serializer = serializers.ImageSerializer(all_images, many=True)
#
#         return Response(data = serializer.data)
#
#
# class ListAllComment(viewsets.ModelViewSet):
#
#     serializer_class = CommentSerializer
#     queryset = Comment.objects.all()
#
#     def get(self, request, format=None):
#
#         all_comment =  Comment.objects.all() # 모든 이미지 출력
#         serializer = serializers.CommentSerializer(all_comment, many=True)
#
#         return Response(data = serializer.data)
#
# class ListAllLikes(viewsets.ModelViewSet):
#
#     serializer_class = LikeSerializer
#     queryset = Like.objects.all()
#
#     def get(self, request, format=None):
#         all_like =  Like.objects.all() # 모든 이미지 출력
#         serializer = serializers.CommentSerializer(all_like, many=True)
#
#         return Response(data = serializer.data)


class Feed(viewsets.ModelViewSet):

    serializer_class = ImageSerializer
    queryset = Image.objects.all()

    def get(self, request, format=None):

        user = request.queryset.user()
        following_users = user.following.all()

        for following_user in following_users:
            print(following_user.images.all()[:2])

        return Response(status=200)
