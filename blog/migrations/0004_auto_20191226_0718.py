# Generated by Django 2.2.7 on 2019-12-26 04:18

import blog.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191225_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='model_pic',
            field=models.ImageField(default='blog/images/already.png', upload_to=blog.models.Post.upload_image),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 26, 4, 18, 15, 683783, tzinfo=utc)),
        ),
    ]