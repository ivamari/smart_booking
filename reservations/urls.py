from django.urls import path, include
from rest_framework.routers import DefaultRouter

from reservations.views.clients import ReservationClientView
from reservations.views.rooms import ReservationRoomView
from reservations.views.reservations import ReservationView

router_reservations = DefaultRouter()
router_reservation_rooms = DefaultRouter()
router_reservation_clients = DefaultRouter()

router_reservations.register(r'', ReservationView, 'reservations')
router_reservation_rooms.register(r'', ReservationRoomView, 'reservation-rooms')
router_reservation_clients.register(r'', ReservationClientView,
                                    'reservation-clients')

urlpatterns = [
    path('reservations/<int:id>/rooms/',
         include(router_reservation_rooms.urls)),
    path('reservations/<int:id>/clients/',
         include(router_reservation_clients.urls)),
    path('reservations/', include(router_reservations.urls)),
]
