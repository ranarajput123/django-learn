from django.db import models

class OrderItem(models.Model):
    label= models.CharField('Label for item')
    isShopifyOrderItem = models.BooleanField('Is the order item from the shopify list?', default=False)
    
    class Meta:
        db_table = 'order-items'