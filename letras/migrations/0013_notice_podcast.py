# Generated by Django 2.2 on 2020-04-05 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letras', '0012_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='podcast',
            field=models.FileField(blank=True, null=True, upload_to='audios/'),
        ),
    ]