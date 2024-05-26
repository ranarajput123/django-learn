from django.db import models
from ..order.models import Order


class ShopifyOrder(models.Model):
    shopifyId = models.CharField('Id of shopify order in shopify platform')
    nsfcId = models.CharField('Shopify NSFC order name/id')
    orderId = models.ForeignKey(Order, verbose_name='Order whom this shopify order details belong to',
                                on_delete=models.CASCADE)

    class Meta:
        db_table = 'shopify-order-details'
