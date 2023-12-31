from rest_framework import serializers
from .models import User, UserInfo


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "nickname",
        )


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = "__all__"


class TinyUserSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = (
            "avator",
            "name",
            "nickname",
            "email",
        )


class PrivateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "avator",
            "name",
            "nickname",
            "email",
            "gender",
            "height",
            "weight",
        )