from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'normal'),
        (STATUS_DELETE, 'delete')
    )

    title = models.CharField(max_length=50, verbose_name='title')
    href = models.URLField(verbose_name='link')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS, verbose_name='status')
    weight = models.PositiveIntegerField(default=1,
                                         choices=zip(range(1, 6), range(1, 6)),
                                         verbose_name='weight',
                                         help_text='The higher the weight, the higher the position')
    owner = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="create time")

    class Meta:
        verbose_name = 'link'
        verbose_name_plural = 'links'


class SlideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEM = (
        (STATUS_SHOW, 'show'),
        (STATUS_HIDE, 'hide')
    )

    SIDE_TYPE = (
        (1, 'HTML'),
        (2, 'latest posts'),
        (3, 'hottest posts'),
        (4, 'recent comments')
    )
    title = models.CharField(max_length=50, verbose_name='title')
    display_type = models.PositiveIntegerField(default=1,
                                               choices=SIDE_TYPE,
                                               verbose_name='show type')
    content = models.CharField(max_length=500, blank=True, verbose_name='content')
    status = models.PositiveIntegerField(default=STATUS_SHOW, choices=STATUS_ITEM,
                                         verbose_name='status')
    owner = models.ForeignKey(User, verbose_name='author', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='create time')

    class Meta:
        verbose_name = 'side bar'
        verbose_name_plural = 'side bars'




