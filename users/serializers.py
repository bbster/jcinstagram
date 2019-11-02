from rest_framework import serializers
from users import models as user_models

#  데이터를 Json 형태로 변환 시켜줌


class ExploreUserSerializer(serializers.ModelSerializer):  # 유저  프로필이미지, 아이디

    class Meta:
        model = user_models.User
        fields = (
            'profile_image',
            'username',
        )
