# Generated by Django 3.0.7 on 2020-08-25 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letras', '0006_auto_20200825_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='banners/'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]