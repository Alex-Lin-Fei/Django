
from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import timezone
# Create your models here.


class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'normal'),
        (STATUS_DELETE, 'delete')
    )

    name = models.CharField(max_length=50, verbose_name="name")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS, verbose_name="status")
    is_nav = models.BooleanField(default=False, verbose_name='is_navigation')
    owner = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="create time")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'normal'),
        (STATUS_DELETE, 'delete')
    )

    name = models.CharField(max_length=10, verbose_name='name')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS, verbose_name='status')
    owner = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="create time")

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'normal'),
        (STATUS_DELETE, 'delete'),
        (STATUS_DRAFT, 'draft')
    )

    title = models.CharField(max_length=255, verbose_name='title')
    abstract = models.CharField(max_length=1024, blank=True, verbose_name='abstract')
    content = models.TextField(verbose_name='content', help_text='content must be MarkDown format')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS, verbose_name='status')
    category = models.ForeignKey(Category, verbose_name='category', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='tag')
    owner = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='create_time', default=timezone.now)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-id']




