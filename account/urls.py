from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from dj_rest_auth.views import LoginView


urlpatterns = [
    path('', views.UserListApiView.as_view()),
    path('register/', views.RegistrationView.as_view()),
    path('activate/', views.ActivationView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('forgot/', views.ForgotPasswordView.as_view()),
]


