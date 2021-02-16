# Generated by Django 3.0.5 on 2021-02-16 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saltfish', '0009_notice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='commodity',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='receiver',
        ),
        migrations.AddField(
            model_name='notice',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='saltfish.Order'),
            preserve_default=False,
        ),
    ]
