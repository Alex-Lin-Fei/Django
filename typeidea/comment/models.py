from django.db import models

from blog.models import Post

# Create your models here.


class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, 'normal'),
        (STATUS_DELETE, 'delete'),
    )
    target = models.ForeignKey(Post, verbose_name='comment target', on_delete=models.CASCADE)
    content = models.CharField(max_length=2000, verbose_name='content')
    nickname = models.CharField(max_length=50, verbose_name='nick name')
    website = models.URLField(verbose_name='website')
    email = models.EmailField(verbose_name='E-mail')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS, verbose_name='status')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='create time')

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'



