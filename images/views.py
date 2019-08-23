from rest_framework import viewsets
from rest_framework.response import Response
from . import models
from . import serializers


class ListAllImages(viewsets.ModelViewSet):

    def get(self, request, format=None):
        all_images =  models.Image.objects.all() # DB에 있는 모든 이미지 가져오기
        serializer = serializers.ImageSerializer(all_images, many=True)

        return Response(data=serializer.data)

    def get_queryset(self, pk):
        return self.queryset.filter(id=self.kwargs.get('pk'))