# Generated by Django 4.2.15 on 2024-09-01 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0004_alter_hotelroom_options_hotelroom_accommodation_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomsettings',
            old_name='hast_wifi',
            new_name='has_wifi',
        ),
    ]
