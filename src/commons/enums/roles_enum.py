from enum import Enum


class RolesEnum(Enum):
    ADMIN = 'admin'
    MEMBER = 'member'

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]
