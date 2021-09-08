from django import db
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, UserManager, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.sessions.models import Session




class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(blank=True)
    fullname = models.TextField(verbose_name='staffname', null=True, blank=True)
    is_staff = models.BooleanField(verbose_name='is_staff', default=True)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='is_active', default=True)
    is_customer = models.BooleanField(verbose_name='is_teller', default=False)

    objects =  UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username
    
    
  
"""Category Table"""  
class Category(models.Model):
    name = models.TextField(null=True, blank=True)
        
    class Meta:
        db_table = 'category'
            
            
            
"""Product Table"""
class Product(models.Model):
    prod_title = models.TextField(null=True, blank=True)
    prod_desc = models.TextField(null=True, blank=True)
    cat_id = models.BigIntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    qty = models.BigIntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'product'


    
