from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter

from . import views
from .views import UserFilmRelationApiView

# router = SimpleRouter()
#
#
# router.register(f'book-relations', UserBookRelationApiView)
router = DefaultRouter()
router.register('', views.PostViewSet)

urlpatterns = [

    # class URLS

    path('', views.FilmListCreateView.as_view()),
    path('<int:pk>/', views.FilmDetailView.as_view()),
    path('film-ration/', views.UserFilmRelationApiView.as_view()),
    path('change/<int:pk>/', views.ChangeApiView.as_view()),


]