# Generated by Django 4.2.15 on 2024-09-07 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0011_accommodationtype_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelroom',
            name='max_adults',
            field=models.IntegerField(default=1, verbose_name='Кол-во подростков'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotelroom',
            name='max_children',
            field=models.IntegerField(default=1, verbose_name='Кол-во детей'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotelroom',
            name='max_guests',
            field=models.IntegerField(default=1, verbose_name='Кол-во гостей'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotelroom',
            name='private',
            field=models.BooleanField(default=False, verbose_name='Приватный'),
        ),
        migrations.AlterField(
            model_name='hotelroom',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]