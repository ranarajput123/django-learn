def formatAmount(amountDecimal):
    if not amountDecimal:
        return '£0'
    return f'£${amountDecimal}'