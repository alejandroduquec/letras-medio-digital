# Generated by Django 2.2 on 2019-04-20 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letras', '0003_auto_20190420_0402'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Linkedin',
            field=models.URLField(blank=True, verbose_name='Perfil Linkedin'),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.URLField(blank=True, verbose_name='Perfil Facebook'),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram',
            field=models.URLField(blank=True, verbose_name='Perfil instagram'),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.URLField(blank=True, verbose_name='Perfil Twitter'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='priority',
            field=models.PositiveIntegerField(choices=[(1, 'Top 1'), (2, 'Top 2'), (3, 'Normal'), (4, 'Columna')]),
        ),
        migrations.AlterField(
            model_name='section',
            name='color_background',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Color Fondo'),
        ),
        migrations.AlterField(
            model_name='section',
            name='color_text',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Color Letra'),
        ),
        migrations.AlterField(
            model_name='section',
            name='order',
            field=models.PositiveIntegerField(verbose_name='Posición en pantalla'),
        ),
    ]