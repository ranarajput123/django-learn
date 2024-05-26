from django.db import models

class Address(models.Model):
    state= models.CharField('State/Province')
    city= models.CharField('City')
    streetAddress= models.CharField('Street Address')
    streetAddress2 = models.CharField('Extra info on Street Address(Street Address 2)')
    postCode= models.CharField('Post Code')
    note = models.CharField('Note for delivery, instructions etc')
    
    class Meta:
        db_table = 'addresses'