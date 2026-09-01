from rest_framework import viewsets, status
from .models import Like
from .serializers import LikeSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        post_id = request.data.get("post")
        user = request.user

        IsLiked = Like.objects.filter(user=user, post_id=post_id)

        if IsLiked.exists():
            IsLiked.delete()
            return Response({
                "message": "Post unliked successfully"
            }, status=status.HTTP_200_OK)

        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

