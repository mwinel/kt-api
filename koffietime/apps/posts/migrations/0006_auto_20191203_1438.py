# Generated by Django 2.2.7 on 2019-12-03 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20191203_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='favorited',
        ),
        migrations.RemoveField(
            model_name='post',
            name='favorited_count',
        ),
    ]
