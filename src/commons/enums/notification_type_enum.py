from enum import Enum

class NotificationTypeEnum(Enum):
    ORDER_REASSIGN = 'order-reassigned'
    
    @classmethod
    def choices(cls):
      return [(key.name,key.value) for key in cls];