from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializers
from users import models as user_models
from users import serializers as user_serializers
from notifications import views as notifications_views


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


class Images(APIView):

    def get(self, request, format=None):

        user = request.user

        following_users = user.following.all()

        image_list = []

        for following_user in following_users:

            user_images = following_user.images.all()[:2]

            for image in user_images:

                image_list.append(image)

        my_images = user.images.all()[:2]

        for image in my_images:

            image_list.append(image)

        sorted_list = sorted(image_list, key=get_key)  # 어느리스트를, 무엇을 기준으로 정렬 한다.

        serializer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):

        user = request.user

        serializer = serializers.InputImageSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(creator=user)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_key(image):
    return image.created_at


class LikeImage(APIView):

    def get(self, request, image_id, format=None):

        likes = models.Like.objects.filter(image__id=image_id)

        like_creators_ids = likes.values('creator_id')

        users = user_models.User.objects.filter(id__in=like_creators_ids)

        serializer = user_serializers.ListUserSerializer(
            users, many=True, context={'request': request}
        )

    def post(self, request, image_id, format=None):

        user = request.user

        #  if문 형식 대신 try catch 형식으로 대신함
        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)  # 해당 이미지가 없으면 404에러

        try:
            preexisting_like = models.Like.objects.get(  # 이미 좋아요가 눌려있을때
                creator=user,
                image=found_image
            )
            return Response(status=status.HTTP_304_NOT_MODIFIED)

        except models.Like.DoesNotExist:  # 좋아요가 없다면

            new_like = models.Like.objects.create(  # 좋아요 추가
                creator=user,
                image=found_image
            )

            notifications_views.create_notification(user, found_image.creator, 'like', found_image
                                                    )
            new_like.save()  # 값 저장
            return Response(status=status.HTTP_201_CREATED)


class UnLikeImage(APIView):

    def delete(self, request, image_id, format=None):
        user = request.user

        #  if문 형식 대신 try catch 형식으로 대신함
        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)  # 해당 이미지가 없으면 404에러

        try:
            preexisting_like = models.Like.objects.get(  # 이미 좋아요가 눌려있을때
                creator=user,
                image=found_image
            )
            preexisting_like.delete()
            return Response(status=status.HTTP_202_ACCEPTED)

        except models.DoesNotExist:
            return Response(status=status.HTTP_304_NOT_MODIFIED)


class CommentOnImage(APIView):  # 이미지에 댓글 달기

    def post(self, request, image_id, format=None):

        user = request.user
        #  if문 형식으로 try catch 사용하기
        try:
            found_image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.CommentSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(creator=user, image=found_image)

            notifications_views.create_notification(
                user, found_image.creator, 'comment', found_image, serializer.data['message'])

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Comment(APIView):

    def delete(self, request, comment_id, format=None):

        user = request.user

        try:
            comment = models.Comment.objects.get(id=comment_id, creator=user)
            comment.delete()
            return Response(stauts=status.HTTP_204_NO_CONTENT)
        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class SearchHashtags(APIView):

    def get(self, request, format=None):

        hashtags = request.query_params.get('hashtags', None)

        if hashtags is not None:

            hashtags = hashtags.split(',')

            # testsplit = '1,2,3,,4음'.split()
            # print(testsplit)음

            images = models.Image.objects.filter(tags__name__in=hashtags).distinct()  # 중복제
            # contains / hashtags가 들어간 단어검색 / 대소문자 구분
            # icontains / 위와 동일 / 대소문자 구분하지 않음
            # exact / 정확히 일치하는것 검색 / 대소문자 구분
            # iexact / 위와동일 / 대소문자 구분하지 않음거

            serializer = serializers.CountImageSerializer(images, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)


class ModerateComments(APIView):

    def get(self, request, image_id, comment_id, format=None):

        user = request.user

        try:
            comment_to_delete = models.Comment.objects.get(id=comment_id, image__id=image_id, image__creator=user)
            comment_to_delete.delete()
        except models.Comment.objects.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ImageDetail(APIView):

    def find_own_image(self, image_id, user):
        try:
            image = models.Image.objects.get(id=image_id, creator=user)
            return image
        except models.Image.DoesNotExist:
            return None

    def get(self, request, image_id, format=None):

        # user = request.user

        try:
            image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ImageSerializer(image)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, image_id, format=None):

        user = request.user

        image = self.find_own_image(image_id, user)

        if image is None:

            return Response(status=status.HTTP_400_BAD_REQUEST)

            serializer = serializers.InputImageSerializer(image, data=request.data, partial=True)

            if serializer.is_valid():

                serializer.save(creator=user)

                return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(data=serializer.data, stauts=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, image_id, format=None):

        user = request.user

        image = self.find_own_image(image_id, user)

        if image is None:

            return Response(status=status.HTTP_401_UNAUTHORIZED)

        image.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

# viewset은 list형식의 데이터 출력시 유리
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
