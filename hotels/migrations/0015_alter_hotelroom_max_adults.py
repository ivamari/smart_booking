# Generated by Django 4.2.15 on 2024-09-11 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0014_hotelpolicy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelroom',
            name='max_adults',
            field=models.IntegerField(verbose_name='Кол-во взрослых'),
        ),
    ]