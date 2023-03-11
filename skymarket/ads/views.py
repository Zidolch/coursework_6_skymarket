from django.shortcuts import get_object_or_404
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.models import Ad, Comment
from ads.permissions import IsOwnerOrAdmin
from ads.serializers import AdDetailSerializer, AdSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination

    default_permission = [IsAuthenticated()]
    permissions = {
        'list': [AllowAny()],
        'update': [IsAuthenticated(), IsOwnerOrAdmin()],
        'partial_update': [IsAuthenticated(), IsOwnerOrAdmin()],
        'destroy': [IsAuthenticated(), IsOwnerOrAdmin()],
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def get_serializer_class(self):
        if self.action in ['list', 'personal_list']:
            return AdSerializer
        else:
            return AdDetailSerializer

    @action(methods=['get'], detail=False, url_path='me')
    def personal_list(self, request, *args, **kwargs):
        self.queryset = Ad.objects.filter(author=request.user)
        return super().list(self, request, *args, **kwargs)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = AdPagination

    default_permission = [IsAuthenticated()]
    permissions = {
        'list': [AllowAny()],
        'update': [IsAuthenticated(), IsOwnerOrAdmin()],
        'partial_update': [IsAuthenticated(), IsOwnerOrAdmin()],
        'destroy': [IsAuthenticated(), IsOwnerOrAdmin()],
    }

    def get_queryset(self):
        ad_id = self.kwargs.get('ad_pk')
        return Comment.objects.filter(ad_id=ad_id)

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def perform_create(self, serializer):
        ad_id = self.kwargs.get('ad_pk')
        ad_instance = get_object_or_404(Ad, pk=ad_id)
        user = self.request.user
        serializer.save(author=user, ad=ad_instance)
