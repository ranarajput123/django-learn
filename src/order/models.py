from django.db import models
from ..commons.models import Customer, BaseCustomer, Address
from ..commons.enums import OrderMethodEnum, PaymentStatusEnum, FulfillmentStatusEnum, OrderStatusEnum


class Order(models.Model):
    orderedAt = models.DateField('When was the order recorded')
    fulfilledAt = models.DateField('When was the order fulfilled at')
    takenBy = models.CharField('Employee name who took the order')
    customer = models.ForeignKey(Customer, verbose_name='Customer for this order', on_delete=models.RESTRICT,
                                 related_name='customer')
    method = models.CharField('Order method', choices=OrderMethodEnum.choices())
    fulfillmentDate = models.DateTimeField('When is the deadline to fulfill the order')
    recipient = models.ForeignKey(BaseCustomer, verbose_name='Recipient details', on_delete=models.RESTRICT,
                                  related_name='Recipient')
    deliveryAddress = models.ForeignKey(Address, verbose_name='Delivery Address for the order',
                                        on_delete=models.RESTRICT)
    paymentStatus = models.CharField('Payment Status of the order', choices=PaymentStatusEnum.choices())
    fulfillmentStatus = models.CharField('Fulfillment Status of the order', choices=FulfillmentStatusEnum.choices())
    content = models.TextField('Content of the order, Free text')
    totalOrderCost = models.PositiveBigIntegerField('Total Cost of the order including delivery charges')
    itemsCost = models.PositiveBigIntegerField('Total Cost of the order items combined excluding delivery charges')
    orderStatus = models.CharField('Order status', choices=OrderStatusEnum.choices())

    class Meta:
        db_table = 'orders'
