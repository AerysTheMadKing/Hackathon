from django.shortcuts import render

from main.permissions import IsAuthorOrAdmin
from . models import Comments
from rest_framework import generics, permissions
from . import serializers
# Create your views here.


class CommentCreateView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetailVies(generics.RetrieveDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    #
    def get_permissions(self):
        if self.request.method == 'DELETE':
            return IsAuthorOrAdmin,
        return permissions.AllowAny(),
