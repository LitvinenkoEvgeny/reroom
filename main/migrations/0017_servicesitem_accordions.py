# Generated by Django 2.1.1 on 2018-09-30 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_catalogitem_to_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicesitem',
            name='accordions',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='main.ServiceItemAccordion'),
            preserve_default=False,
        ),
    ]