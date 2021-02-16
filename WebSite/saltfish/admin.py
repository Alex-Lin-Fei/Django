from django.contrib import admin
from .models import Commodity, UserInfo, Category, Record, Order, Message, Comment, Notice


# Register your models here.


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'grade', 'faculty', 'register_time')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
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
        'quantity',
        'picture',
        'category',
        'departure',
        'views',
        'likes',
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
    list_display = (
        'buyer', 'commodity',
        'number', 'status',
        'address', 'create_time',
        'delivery_time', 'receipt_time'
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'sender', 'receiver',
        'status', 'content',
        'create_time',
    )


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        'order', 'status',
        'type', 'create_time',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'publisher', 'commodity',
        'content', 'create_time',
    )
