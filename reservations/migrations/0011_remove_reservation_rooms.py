# Generated by Django 4.2.15 on 2024-09-21 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0010_reservation_rooms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='rooms',
        ),
    ]
