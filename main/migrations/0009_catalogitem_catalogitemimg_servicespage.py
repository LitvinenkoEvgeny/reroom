# Generated by Django 2.1.1 on 2018-09-24 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20180924_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_on_main', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=500)),
                ('type', models.CharField(choices=[('design', 'Дизайн'), ('house', 'Ремонт квартир и домов'), ('office', 'Ремонт офисоф'), ('construction', 'Строительство домов')], max_length=80)),
                ('main_img', models.ImageField(blank=True, upload_to='admin/services')),
                ('top_left', models.DateField()),
                ('top_right', models.CharField(max_length=500)),
                ('bottom_left', models.CharField(max_length=500)),
                ('bottom_right', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='CatalogItemImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_field', models.ImageField(blank=True, upload_to='admin/services')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('catalog_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.CatalogItem')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services_page_title', models.CharField(max_length=200)),
                ('single_item_top_left_heading', models.CharField(max_length=500)),
                ('single_item_top_right_heading', models.CharField(max_length=500)),
                ('single_item_bottom_left_heading', models.CharField(max_length=500)),
                ('single_item_bottom_right_heading', models.CharField(max_length=500)),
            ],
        ),
    ]