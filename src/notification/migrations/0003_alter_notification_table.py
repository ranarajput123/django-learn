# Generated by Django 5.0.6 on 2024-05-26 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='notification',
            table='notifications',
        ),
    ]