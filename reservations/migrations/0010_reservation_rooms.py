# Generated by Django 4.2.15 on 2024-09-21 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0017_alter_hotelroomstatus_created_at_and_more'),
        ('reservations', '0009_remove_reservation_rooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='rooms',
            field=models.ManyToManyField(through='reservations.ReservationRoom', to='hotels.hotelroom'),
        ),
    ]
