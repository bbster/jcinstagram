from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializers


class ListAllImages(APIView):

    def get(self, request, format=None):

        all_images = models.Image.objects.all()

        serializer = serializers.ImageSerializer(all_images, many=True)

        return Response(data=serializer.data)


class ListAllComments(APIView):

    def get(self, request, format=None):

        # user_id = request.user.id  # 로그인 유저의 댓글 보기위한 user id값

        all_comments = models.Comment.objects.all()  # filter(creator=user_id) 자신의 댓글 확인 가능

        serializer = serializers.CommentSerializer(all_comments, many=True)

        return Response(data=serializer.data)


class ListAllLikes(APIView):

    def get(self, request, format=None):

        all_likes = models.Like.objects.all()  # like 모델의 모든 오브젝트 정보를 all_likes 에 저장

        serializer = serializers.LikeSerializer(all_likes, many=True)

        return Response(data=serializer.data)


class Feed(APIView):

    def get(self, request, format=None):

        user = request.user

        following_users = user.following.all()

        image_list = []

        for following_user in following_users:

            user_images = following_user.images.all()[:2]

            for image in user_images:

                image_list.append(image)

        sorted_list = sorted(image_list, key=get_key)  # 어느리스트를, 무엇을 기준으로 정렬 한다.

        print(sorted_list)

        serializer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(serializer.data)


def get_key(image):
    return image.created_at


class LikeImage(APIView):

    def post(self, request, image_id, format=None):

        print(image_id)

        return Response(status=200)



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
