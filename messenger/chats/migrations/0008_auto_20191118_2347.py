# Generated by Django 2.2.5 on 2019-11-18 23:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0007_auto_20191118_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 18, 23, 47, 31, 782349), verbose_name='Message creation time'),
        ),
    ]