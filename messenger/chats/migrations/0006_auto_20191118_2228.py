# Generated by Django 2.2.5 on 2019-11-18 22:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0005_message_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 18, 22, 28, 50, 321635, tzinfo=utc), verbose_name='Message creation time'),
        ),
    ]
