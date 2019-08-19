from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers

class ListAllImages(APIView):

    def get(self, request, format=None):
        all_images =  models.Image.objects.all() # DB에 있는 모든 이미지 가져오기
        serializer = serializers.ImageSerializer(all_images, many=True)

        return Response(data=serializer.data)