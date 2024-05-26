from enum import Enum

class OrderStatusEnum(Enum):
    CANCELLED = 'Cancelled'
    ACTIVE = 'Active'
    DELETED = 'Deleted'
  
    @classmethod
    def choices(cls):
      return [(key.name,key.value) for key in cls];
