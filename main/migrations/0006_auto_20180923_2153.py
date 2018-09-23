# Generated by Django 2.1.1 on 2018-09-23 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180923_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpage',
            name='fifth_screen_image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Картинка пятого экрана'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='first_image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Картинка, отображающаяся на главной странице'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='fourth_screen_image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Картинка четвертого экрана'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='second_screen_image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Картинка второго экрана'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='third_screen_image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Картинка третьего экрана'),
        ),
    ]