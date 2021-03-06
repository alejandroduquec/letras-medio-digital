# Generated by Django 3.0.7 on 2020-08-25 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letras', '0005_auto_20200825_0251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name': 'Banner publiciario', 'verbose_name_plural': 'Banners publicitarios'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Compañía', 'verbose_name_plural': 'Datos de la compañía'},
        ),
        migrations.AddField(
            model_name='banner',
            name='video',
            field=models.FileField(default='', upload_to='videos/'),
            preserve_default=False,
        ),
    ]
