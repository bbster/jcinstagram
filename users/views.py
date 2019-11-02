from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializers


class ExplorerUsers(APIView):

    def get(self, request, format=None):

        last_user = models.User.objects.all()[:5]

        serializer = serializers.ExploreUserSerializer(last_user, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
