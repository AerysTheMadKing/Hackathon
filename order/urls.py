from django.urls import path

from order import views

urlpatterns = [

    path('', views.OrderCreateListAPIVIew.as_view(), name="cart"),
    path('order/<int:pk>/', views.OrderRetrieve.as_view()),
    path('order_item/<int:pk>/', views.OrderItemDelView.as_view()),


]