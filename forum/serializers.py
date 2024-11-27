from rest_framework import serializers
from .models import Topic, Comment
from django.contrib.auth.models import User

class TopicSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Topic
        fields = ['id', 'title', 'content', 'created_at', 'user']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    parent_comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), required=False)

    class Meta:
        model = Comment
        fields = ['id', 'topic', 'content', 'created_at', 'user', 'parent_comment']
