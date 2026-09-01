from rest_framework import viewsets, filters
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from config.permissions import IsAuthorOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related("user", "post").all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ["text"]
    search_fields = ["text"]
    ordering_fields = ["created_at"]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)