from enum import Enum

class PaymentStatusEnum(Enum):
    INVOICE_SENT = 'Square Invoice Sent'
    INVOICE_PAID = 'Square Invoice Paid'
    PAID_BY_CARD = 'Paid By Card'
    PAID_BY_CASH = 'Paid By Cash'
    GIFT = 'Gift'
    PENDING = 'Payment Pending'
    
    @classmethod
    def choices(cls):
      return [(key.name,key.value) for key in cls];