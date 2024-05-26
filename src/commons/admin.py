from django.contrib import admin
from .models import Address, Customer, OrderItem

admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(OrderItem)
