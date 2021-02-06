from django.db import models


# Create your models here.


class Student(models.Model):
    SEX_ITEMS = [
        (1, 'male'),
        (2, 'female'),
        (0, 'unknown')
    ]
    STATUS_ITEMS = [
        (0, 'apply'),
        (1, 'pass'),
        (2, 'refuse')
    ]

    name = models.CharField(max_length=128, verbose_name="name")
    sex = models.IntegerField(choices=SEX_ITEMS, verbose_name="sex")
    profession = models.CharField(max_length=128, verbose_name="profession")
    email = models.EmailField(max_length=128, verbose_name="E-mail")
    qq = models.CharField(max_length=128, verbose_name='QQ')
    phone = models.CharField(max_length=11, verbose_name="telephone")

    status = models.IntegerField(choices=STATUS_ITEMS, default=0, verbose_name="Audit State")
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Create Time")

    def __str__(self):
        return '<Student: {}>'.format(self.name)

    @property
    def sex_show(self):
        return dict(self.SEX_ITEMS)[self.sex]

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        verbose_name = verbose_name_plural = "student information"


