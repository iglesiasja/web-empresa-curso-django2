# Generated by Django 3.2.12 on 2022-03-04 18:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 4, 18, 40, 24, 786883, tzinfo=utc), verbose_name='Publicacion'),
        ),
    ]
