# Generated by Django 5.0.6 on 2024-05-26 18:51

import src.commons.enums.roles_enum
import src.commons.enums.store_names_enum
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='refreshToken',
        ),
        migrations.AddField(
            model_name='user',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='isStaff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='refresh_token',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Refresh token'),
        ),
        migrations.AlterField(
            model_name='user',
            name='firstName',
            field=models.CharField(max_length=30, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastName',
            field=models.CharField(max_length=30, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=src.commons.enums.roles_enum.RolesEnum.choices(), max_length=20, verbose_name='Role assigned to the user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='store',
            field=models.CharField(choices=src.commons.enums.store_names_enum.StoresEnum.choices(), max_length=20, verbose_name='Store Assigned to User'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
