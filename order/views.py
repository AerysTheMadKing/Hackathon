from rest_framework import generics, permissions

from order import serializers
from order.models import Order

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from order.models import OrderItem, Order
from order.serializers import OrderSerializer, OrderItemSerializer
from main.models import Film

from .tasks import send_mail_func


class OrderCreateListAPIVIew(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        order_data = serializer.validated_data
        order = Order.objects.create(
            user=self.request.user,
            status=order_data.get('status', 'IN_PROGRESS'),
            total_price=order_data.get('total_price', 0),
        )

        order_items_data = order_data.get('order_item')
        if order_items_data:
            order_items = []
            for item_data in order_items_data:
                order_items.append(OrderItem(
                    order=order,
                    films=item_data['films'],
                ))
            OrderItem.objects.bulk_create(order_items)

        send_mail_func.delay()
        print(send_mail_func.delay())
        serializer.instance = order


class OrderRetrieve(generics.RetrieveAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)


class OrderItemDelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
