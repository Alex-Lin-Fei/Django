from django.contrib import admin
from .models import Commodity, UserInfo, Category, Record, Order
# Register your models here.


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'grade', 'faculty', 'register_time')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    list_display = ('name', 'slug')


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'commodity', 'type', 'create_time')


@admin.register(Commodity)
class CommodityAdmin(admin.ModelAdmin):
    list_display = (
        'owner',
        'tag',
        'price',
        'picture',
        'category',
        'departure',
        'create_time',
    )

    fieldsets = (
        ('basic configuration', {
            'description': 'basic configuration description',
            'fields': (
                'tag',
                'price',
                'picture',
                'owner',
                'category',
            ),
        }),
        ('content', {
            'fields': (
                'description',
                'quantity',
                'departure',
            ),
        }),
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'commodity', 'number', 'status', 'address', 'create_time', 'receipt_time')

