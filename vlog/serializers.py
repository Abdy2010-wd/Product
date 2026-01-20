from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Post
        fields = ['id', 'title', 'author', 'body', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Comment
        fields = ['id', 'author', 'post', 'body', 'created_at', 'updated_at']
