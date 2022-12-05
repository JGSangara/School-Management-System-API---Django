from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.validators import MinLengthValidator
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from PIL import Image

# Create your models here.


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **other_fields):

        if not email:
            raise ValueError('You must provide an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **other_fields):

        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **other_fields)

    def create_superuser(self, email, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self.create_user(
            email,
            password=password,
            **other_fields
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_student = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    preferred_name = models.CharField(max_length=150, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    discord_name = models.CharField(max_length=150, blank=True)
    github_username = models.CharField(max_length=150, blank=True)
    codepen_username = models.CharField(max_length=150, blank=True)
    fcc_profile_url = models.CharField(max_length=150, blank=True)
    LEVELS = (
        (1, 'Level One'),
        (2, 'Level Two'),
        (3, 'Level Three'),
    )

    current_level = models.IntegerField(choices=LEVELS)
    phone = models.CharField(max_length=15, blank=True)
    timezone = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'