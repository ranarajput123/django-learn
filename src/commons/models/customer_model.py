from django.db import models
from .address_model import Address
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class BaseCustomer(models.Model):
    firstName = models.CharField('First Name')
    lastName = models.CharField('Last Name')
    phone = models.CharField('Phone number')

    class Meta:
        verbose_name = _("BaseCustomer")
        verbose_name_plural = _("BaseCustomers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("BaseCustomer_detail", kwargs={"pk": self.pk})
    
    class Meta:
        db_table = 'base-customers'

class Customer (BaseCustomer):
    email = models.EmailField('Email')
    billingAddress = models.ForeignKey(Address,on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'customers'