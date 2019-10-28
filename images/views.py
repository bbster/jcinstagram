from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializers


# viewset은 list형식의 데이터 출력시 유
# class ListAllImages(viewsets.ModelViewSet):
#
#     serializer_class = ImageSerializer  # 시리얼라이저
#     queryset = Image.objects.all()  # 모델
#
#     # @action(detail=True, methods=['get'])
#     def get(self, request, format=None):
#         all_images = Image.objects.all()  # 모든 이미지 출력
#         serializer = serializers.ImageSerializer(all_images, many=True)
#         return Response(data=serializer.data)
#
#
# class ListAllComment(viewsets.ModelViewSet):
#
#     serializer_class = CommentSerializer
#     queryset = Comment.objects.all()
#
#     def get(self, request, format=None):
#
#         # user_id = request.user.id  # user id 값 불러와서 user_id에 저장
#         all_comment = Comment.objects.all()  # 모든 댓글 출력 DB에서 불러온 user id 값으로 필터링
#         serializer = serializers.CommentSerializer(all_comment, many=True)
#
#         return Response(data=serializer.data)
#
#
# class ListAllLikes(viewsets.ModelViewSet):
#
#     serializer_class = LikeSerializer
#     queryset = Like.objects.all()
#
#     def get(self, request, format=None):
#         all_like = Like.objects.all()  # 모든 좋아요 출력
#
#         serializer = serializers.CommentSerializer(all_like, many=True)
#
#         return Response(data=serializer.data)

class ListAllImage(APIView):

    def get(self, request, format=None):

        all_images = models.Image.objects.all()

        serializer = serializers.ImageSerializer(all_images, many=True)

        return Response(data=serializer.data)


class ListAllComment(APIView):

    def get(self, request, format=None):

        all_comments = models.Comment.objects.all()

        serializer = serializers.CommentSerializer(all_comments, many=True)

        return Response(data=serializer.data)


class ListAllLike(APIView):

    def get(self, request, format=None):

        all_likes = models.Like.objects.all()

        serializer = serializers.LikeSerializer(all_likes, many=True)

        return Response(data=serializer.data)