from django.db import models
from ..commons.models import OrderItem
from ..order.models import Order


class OrderDetails(models.Model):
    item = models.ForeignKey(OrderItem, verbose_name='Order item', on_delete=models.RESTRICT)
    quantity = models.IntegerField('Quantity of ordered item')
    orderId = models.ForeignKey(Order, verbose_name='Order containing this item', on_delete=models.CASCADE)

    class Meta:
        db_table = 'order-details'
