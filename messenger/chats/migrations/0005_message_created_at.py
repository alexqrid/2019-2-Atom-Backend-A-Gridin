# Generated by Django 2.2.5 on 2019-11-18 22:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_auto_20191118_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 18, 22, 26, 35, 768289, tzinfo=utc), verbose_name='Message creation time'),
        ),
    ]
