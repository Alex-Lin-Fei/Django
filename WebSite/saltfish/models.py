from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=16, unique=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    FRESH_MAN = 1
    SOPHOMORE = 2
    JUNIOR = 3
    SENIOR = 4
    GRADE_ITEMS = (
        (FRESH_MAN, 'fresh man'),
        (SOPHOMORE, 'sophomore'),
        (JUNIOR, 'junior'),
        (SENIOR, 'senior'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='profile_images',
                                default="http://lorempixel.com/300/300/people/")
    # email = models.EmailField(max_length=32, verbose_name='E-mail')
    phone = models.CharField(max_length=32, verbose_name='telephone', default='')
    grade = models.PositiveIntegerField(default=FRESH_MAN,
                                        choices=GRADE_ITEMS)
    faculty = models.CharField(max_length=32)
    register_time = models.DateTimeField(auto_now_add=True, verbose_name='register time')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = verbose_name_plural = 'user information'


class Commodity(models.Model):
    tag = models.CharField(max_length=64, blank=False)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=128)
    picture = models.ImageField(upload_to='commodity_images',
                                default="http://lorempixel.com/300/300/people/")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='quantity')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='create_time')
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    departure = models.CharField(max_length=64)
    numberOfComments = models.IntegerField(default=0, verbose_name='number of comments')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name_plural = 'commodities'


class Record(models.Model):
    RELEASED = 1
    BOUGHT = 2
    SOLD = 3
    CART = 4
    COLLECTION = 5
    TYPE = (
        (RELEASED, 'released'),
        (BOUGHT, 'bought'),
        (SOLD, 'sold'),
        (CART, 'cart'),
        (COLLECTION, 'collection')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    type = models.PositiveIntegerField(choices=TYPE, default=RELEASED)

    class Meta:
        verbose_name_plural = 'records'


class Order(models.Model):
    UNDELIVERED = 1
    DISPATCHED = 2
    UNEVALUATED = 3
    REFUND = 4
    COMPLETED = 5

    STATUS_ITEMS = (
        (UNDELIVERED, 'To be delivered'),
        (DISPATCHED, 'To be received'),
        (UNEVALUATED, 'To be evaluated'),
        (REFUND, 'goods of rejected'),
        (COMPLETED, 'completed'),
    )

    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    number = models.IntegerField(default=0, blank=True)
    status = models.PositiveIntegerField(choices=STATUS_ITEMS, default=UNDELIVERED)
    address = models.CharField(max_length=64, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    delivery_time = models.DateTimeField(blank=True, default=timezone.now)
    receipt_time = models.DateTimeField(blank=True, default=timezone.now)

    class Meta:
        verbose_name_plural = 'orders'


class Message(models.Model):
    UNREAD = 1
    READ = 2
    STATUS_ITEM = (
        (UNREAD, 'unread'),
        (READ, 'read'),
    )

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    content = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.PositiveIntegerField(choices=STATUS_ITEM, default=UNREAD)

    class Meta:
        verbose_name_plural = 'messages'


class Notice(models.Model):
    UNREAD = 1
    READ = 2
    STATUS_ITEM = (
        (UNREAD, 'unread'),
        (READ, 'read'),
    )

    BOUGHT_SELLER = 1
    BOUGHT_BUYER = 2
    SEND_SELLER = 3
    SEND_BUYER = 4
    RECEIVER_SELLER = 5
    RECEIVER_BUYER = 6

    TYPE_ITEM = (
        (BOUGHT_SELLER, 'bought_seller'),
        (BOUGHT_BUYER, 'bought_buyer'),
        (SEND_SELLER, 'send_seller'),
        (SEND_BUYER, 'send_buyer'),
        (RECEIVER_SELLER, 'receiver_seller'),
        (RECEIVER_BUYER, 'receiver_buyer'),
    )

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.PositiveIntegerField(choices=STATUS_ITEM, default=UNREAD)
    type = models.PositiveIntegerField(choices=TYPE_ITEM)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'notices'


class Comment(models.Model):
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'comments'
