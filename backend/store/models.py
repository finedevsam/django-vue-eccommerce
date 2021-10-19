from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, UserManager, BaseUserManager
from django.utils.translation import ugettext_lazy as _

from io import BytesIO
from PIL import Image
from django.core.files import File



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
    slug = models.SlugField()
        
    class Meta:
        ordering = ('name',)
        db_table = 'category'
        
    def __str__(self):
        return "{}".format(self.name)
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
            
            
            
"""Product Table"""
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.TextField(null=True, blank=True)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-date_created',)
        db_table = 'product'
        
    def __str__(self):
        return "{}".format(self.name)
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
            
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail


    
