from rest_framework import serializers
from cube.models import User, Cube, Content, CubeUser, ContentCube,ContentUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'city')


class CubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cube
        fields = ('id', 'user_id', 'name', )


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('id', 'user_id', 'link')


class CubeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CubeUser
        fields = ('id', 'user_id', 'cube_id')


class ContentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentUser
        fields = ('id', 'user_id', 'content_id', )


class ContentCubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentCube
        fields = ('id', 'user_id', 'cube_id', 'content_id')