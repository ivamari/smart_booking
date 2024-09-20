from reservations.models.reservations import ReservationRoom


class ReservationUpdateService:
    def update_instance(self, validated_data, instance):
        rooms = validated_data.pop('rooms')

        instance.start_date = validated_data.get('start_date',
                                                 instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.adults = validated_data.get('adults', instance.adults)
        instance.children = validated_data.get('children', instance.children)
        instance.save()

        ReservationRoom.objects.filter(reservation=instance).delete()

        for room in rooms:
            ReservationRoom.objects.create(reservation=instance, room=room,
                                           status_id='not_checked_in')

        return instance
