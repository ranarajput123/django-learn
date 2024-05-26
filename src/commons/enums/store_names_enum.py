from enum import Enum


class StoresEnum(Enum):
    BELGRAVIA_BOUTIQUE = 'belgravia boutique'
    MAYFAIR_BOUTIQUE = 'mayfair boutique'
    STUDIO = 'studio'
    HARRODS = 'harrods'
    SHOPIFY = 'shopify-store'

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls];
