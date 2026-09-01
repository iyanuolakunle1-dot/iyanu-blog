from .models import Post
from rest_framework import serializers
from accounts.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ["id", "title", "content", "user", "picture", "created_at", "updated_at"]
        read_only_fields = ["id", "user", "created_at", "updated_at"]

