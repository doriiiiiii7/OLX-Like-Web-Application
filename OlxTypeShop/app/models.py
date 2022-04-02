from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=False)
    email = models.CharField(max_length=200, null=True, blank=False)
    phone_number = models.CharField(max_length=10, null=True)

    class Meta:
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.name


class Product(models.Model):
    CURRENCY_CHOICES = (
        ('LEI', 'LEI'),
        ('€', '€'),
    )

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, unique=False)
    description = models.TextField(blank=True)
    added_by = models.ForeignKey(Customer, on_delete=models.CASCADE, unique=False)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=5, choices=CURRENCY_CHOICES, default='LEI')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return self.title


