# Generated by Django 2.2 on 2022-03-04 20:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20220304_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 4, 20, 43, 42, 867311, tzinfo=utc), verbose_name='Publicacion'),
        ),
    ]
