# Generated by Django 2.0.2 on 2022-03-02 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20220302_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(null=True, upload_to='services', verbose_name='Imagen'),
        ),
    ]
