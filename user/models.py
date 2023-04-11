from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None, **other_fields,):

        if not email:
            raise ValueError('You must provide an email address')
        if not username:
            raise ValueError('You must provide a name and surname')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **other_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password=password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, verbose_name='Name')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Email address')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]
