from django.db import transaction


class ReservationClientFactory:
    def set_client_as_main(self, reservation_client):
        with transaction.atomic():
            reservation_client.is_main_client = True
            reservation_client.save()

            reservation_client.reservation.client = reservation_client.client
            reservation_client.reservation.save()

            reservation_client.reservation.clients.exclude(
                id=reservation_client.id).update(is_main_client=False)
