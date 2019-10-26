from rest_framework import viewsets
from rest_framework.response import Response
from images.serializers import ImageSerializer, CommentSerializer, LikeSerializer
from .models import Image, Comment, Like
from . import serializers


class ListAllImages(viewsets.ModelViewSet):

    serializer_class = ImageSerializer  # 시리얼라이저
    queryset = Image.objects.all()  # 모델

    # @action(detail=True, methods=['get'])
    def get(self, request, format=None):
        all_images = Image.objects.all()  # 모든 이미지 출력
        serializer = serializers.ImageSerializer(all_images, many=True)
        return Response(data=serializer.data)


class ListAllComment(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get(self, request, format=None):

        all_comment = Comment.objects.all()  # 모든 이미지 출력
        serializer = serializers.CommentSerializer(all_comment, many=True)

        return Response(data=serializer.data)


class ListAllLikes(viewsets.ModelViewSet):

    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def get(self, request, format=None):
        all_like = Like.objects.all()  # 모든 이미지 출력
        serializer = serializers.CommentSerializer(all_like, many=True)

        return Response(data=serializer.data)


# class Feed(viewsets.ModelViewSet):
#
#     serializer_class = ImageSerializer
#     queryset = Image.objects.all()
#
#     def get(self, request, format=None):
#
#         user = request.queryset.user()
#
#         following_users = user.following.all()
#
#         image_list = []
#
#         for following_user in following_users:
#
#             user_images = following_user.images.all()[:2]
#
#             for image in user_images:
#
#                 image_list.append(image)  #  append는 리스트 제일뒤에 추가
#                                               ex) 리스트형식이면 리스트형식 그대로 추가
#                                           #  extend는 리스트 확장 리스트형식의 appending
#
#         sorted_list = sorted(image_list, key=get_key) # 1. 어느리스트를 정렬할것인가
#                                                       # 2. 어떻게 정렬 할것인가
#                                                       # 3. return값을 기준으로 정렬
#         serializer = serializers.ImageSerializer(sorted_list, many=True)
#
#         return Response(serializer.data)
#
# def get_key(image):
#      return image.created_at
