# Generated by Django 2.1.1 on 2018-09-24 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_catalogitem_catalogitemimg_servicespage'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogitem',
            name='service',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='main.ServicesPage'),
            preserve_default=False,
        ),
    ]