from reservations.models.reservations import (Reservation, ReservationClient,
                                              ReservationRoom)


class ReservationCreatorService:

    def create_instance(self, validated_data):
        rooms = validated_data.pop('rooms')
        reservation = Reservation.objects.create(**validated_data)

        client = validated_data.get('client')

        ReservationClient.objects.create(reservation=reservation,
                                         client=client,
                                         is_main_client=True)

        for room in rooms:
            ReservationRoom.objects.create(reservation=reservation, room=room,
                                           status_id='not_checked_in')

        return reservation


