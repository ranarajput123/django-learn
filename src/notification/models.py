from django.db import models
from ..user.models import User
from ..order.models import Order
from ..commons.enums import NotificationTypeEnum


class Notification(models.Model):
    message = models.TextField('Notification text')
    user = models.ForeignKey(User, verbose_name='User the notification belongs to', on_delete=models.CASCADE,
                             related_name='notification_for')
    type = models.CharField('Notification type', choices=NotificationTypeEnum.choices())
    orderId = models.ForeignKey(Order, verbose_name='Order Id for which the notification is', on_delete=models.CASCADE)
    actor = models.ForeignKey(User, verbose_name='Who performed the action which caused the notification',
                              on_delete=models.SET_NULL, null=True, related_name='notification_by')
    viewed = models.BooleanField('Is notification seen ?', default=False)

    class Meta:
        db_table = 'notifications'
