from django.db import models

from account.models import CustomUser

from order.utils import ORDER_STATUS

from main.models import Film


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=ORDER_STATUS,) # need to set default parameters
    total_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    """нужно добавить created_at,"""

    class Meta:
        db_table = 'order'

    def __str__(self):
        return f'{self.user}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item', null=True, blank=True)
    films = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='order_item_film', null=True, blank=True)
    """нужно добавить created_at,"""

    class Meta:
        db_table = 'order_item'

    def __str__(self):
        return f'{self.order}'