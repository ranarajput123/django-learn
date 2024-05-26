from enum import Enum

class OrderMethodEnum(Enum):
    DELIVERY = 'delivery'
    COLLECTION = 'collection'
    
    @classmethod
    def choices(cls):
      return [(key.name,key.value) for key in cls];