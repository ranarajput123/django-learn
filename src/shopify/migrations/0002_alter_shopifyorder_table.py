# Generated by Django 5.0.6 on 2024-05-26 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='shopifyorder',
            table='shopify-order-details',
        ),
    ]
