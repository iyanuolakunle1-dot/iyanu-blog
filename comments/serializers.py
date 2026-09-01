from .models import Comment
from rest_framework import serializers
from accounts.serializers import UserSerializer
from posts.serializers import PostSerializer
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ["id", "text", "post", "user", "created_at", "updated_at"]
        read_only_fields = ["id", "user", "post", "created_at", "updated_at"]

