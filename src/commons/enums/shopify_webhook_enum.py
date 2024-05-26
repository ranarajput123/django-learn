from enum import Enum

class ShopifyWebhookTypesEnum(Enum):
    CREATED = 'created'
    UPDATED = 'updated'
    
    @classmethod
    def choices(cls):
      return [(key.name,key.value) for key in cls];