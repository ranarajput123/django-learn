# Generated by Django 5.0.6 on 2024-05-26 20:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopifyOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopifyId', models.CharField(verbose_name='Id of shopify order in shopify platform')),
                ('nsfcId', models.CharField(verbose_name='Shopify NSFC order name/id')),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='Order whom this shopify order details belong to')),
            ],
        ),
    ]
