from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from ..commons.enums import StoresEnum, RolesEnum


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        print(extra_fields.get('role'))
        extra_fields.setdefault('is_superuser', extra_fields.get('role') == RolesEnum.ADMIN.name)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField('First name', max_length=30)
    last_name = models.CharField('Last name', max_length=30)
    email = models.EmailField('Email Of The user', unique=True)
    store = models.CharField(max_length=20, choices=StoresEnum.choices(), verbose_name='Store Assigned to User')
    role = models.CharField(max_length=20, choices=RolesEnum.choices(), verbose_name='Role assigned to the user')
    password = models.CharField('Password', max_length=128)
    refresh_token = models.CharField('Refresh token', max_length=255, blank=True, null=True)
    emailVerified = models.BooleanField('Is The email of user verified', default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role', 'store']

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.email

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True
