from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'description', 'added_by', 'image', 'price', 'currency', 'created', 'updated')

admin.site.register(Category)