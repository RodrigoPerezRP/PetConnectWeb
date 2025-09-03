from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager
)


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Debes tener un correo electronico")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(default='')
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True, default='profiles/profile.png')
    username = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=9, null=True, blank=True)
    objects = CustomUserManager()   
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ["-date_joined"]

    def __str__(self):
        return f"{self.username}"
    

    def save(self,*args,**kwargs):
        self.slug = slugify(self.username)
        self.password = make_password(self.password)
        super(User, self).save(*args,**kwargs)