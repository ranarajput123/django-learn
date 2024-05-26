from enum import Enum

class TimeEnum(Enum):
    AM = 'am'
    PM = 'pm'
    NOT_SPECIFIED = 'not-specified'
    
    @classmethod
    def choices(cls):
      return [(key.name,key.value) for key in cls];