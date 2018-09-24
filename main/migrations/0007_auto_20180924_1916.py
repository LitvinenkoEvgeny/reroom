# Generated by Django 2.1.1 on 2018-09-24 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20180923_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.TextField(max_length=50)),
                ('email', models.TextField(max_length=100)),
                ('addr', models.TextField(max_length=500)),
                ('instagram_text', models.TextField(max_length=500)),
                ('instagram_link', models.URLField(max_length=500)),
                ('development', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.RemoveField(
            model_name='indexpage',
            name='contact_info',
        ),
        migrations.AlterField(
            model_name='indexpage',
            name='fifth_screen_image',
            field=models.ImageField(blank=True, upload_to='admin/index', verbose_name='Картинка пятого экрана'),
        ),
        migrations.AlterField(
            model_name='indexpage',
            name='first_image',
            field=models.ImageField(blank=True, upload_to='admin/index', verbose_name='Картинка, отображающаяся на главной странице'),
        ),
        migrations.AlterField(
            model_name='indexpage',
            name='fourth_screen_image',
            field=models.ImageField(blank=True, upload_to='admin/index', verbose_name='Картинка четвертого экрана'),
        ),
        migrations.AlterField(
            model_name='indexpage',
            name='third_screen_image',
            field=models.ImageField(blank=True, upload_to='admin/index', verbose_name='Картинка третьего экрана'),
        ),
    ]