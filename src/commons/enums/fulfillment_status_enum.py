from enum import Enum

class FulfillmentStatusEnum(Enum):
    DELIVERED = 'Delivered'
    COLLECTED = 'Collected'
    RETURNED = 'Returned to boutique'
    SAFE_PLACE = 'Left in safe place'
    NEIGHBOR = 'Left with neighbors'
    DISPATCH_READY = 'Ready to dispatch'
    OUT_FOR_DELIVERY = 'Out for delivery'
    
    @classmethod
    def choices(cls):
      return [(key.name,key.value) for key in cls];