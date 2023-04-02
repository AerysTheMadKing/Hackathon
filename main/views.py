from rest_framework import permissions
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Film, UserFilmRelation
from . import serializers
from . import serializers
from .serializers import UserFilmRelationSerializers, ChangeSerializers, FilmListSerializer


class StandartResultPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    max_page_size = 1000


class PostViewSet(ModelViewSet):
    queryset = Film.objects.all()
    pagination_class = StandartResultPagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title',)
    filterset_fields = ('title', 'year')


# class FilmListCreateView(generics.ListCreateAPIView):
#     queryset = Film.objects.all()
#     serializer_class = serializers.FilmListSerializer
#     # permission_classes = (permissions.IsAdminUser,)
#     filter_backends = (SearchFilter, DjangoFilterBackend)
#     search_fields = ('title',)
#     filterset_fields = ('title', 'year')
#
#     def get_object(self):
#         obj, _ = UserFilmRelation.objects.get_or_create(user=self.request.user,
#                                                         films_id=self.kwargs['films'])
#         return obj

# def get_permissions(self):
#     if self.request.method == 'POST':
#         return permissions.IsAdminUser(),
#     return permissions.AllowAny(),

# def get_serializer_class(self):
#     if self.request.method == 'GET':
#         return serializers.FilmListSerializer
#     return serializers.FilmDetailSerializer

from main.utils import get_total_rating


class FilmListCreateView(generics.ListAPIView):
    serializer_class = FilmListSerializer

    def get_queryset(self):
        queryset = Film.objects.all()
        for film in queryset:
            film.rating = get_total_rating(film.id)
        return queryset


class FilmDetailView(generics.RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = serializers.FilmDetailSerializer

    def get_queryset(self):
        queryset = Film.objects.all()
        queryset.prefetch_related('comments__user')
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.rating = get_total_rating(instance.id)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UserFilmRelationApiView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = UserFilmRelation.objects.all()
    serializer_class = UserFilmRelationSerializers


class ChangeApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserFilmRelation.objects.all()
    serializer_class = ChangeSerializers
