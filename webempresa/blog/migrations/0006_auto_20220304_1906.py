# Generated by Django 2.2 on 2022-03-04 19:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 4, 19, 6, 4, 86645, tzinfo=utc), verbose_name='Publicacion'),
        ),
    ]
