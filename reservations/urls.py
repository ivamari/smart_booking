from django.urls import path, include
from rest_framework.routers import DefaultRouter

from reservations.views.reservation_rooms import ReservationRoomView
from reservations.views.reservations import ReservationView

router_reservations = DefaultRouter()
router_reservation_rooms = DefaultRouter()

router_reservations.register(r'', ReservationView, 'reservations')
router_reservation_rooms.register(r'', ReservationRoomView, 'reservation-rooms')

urlpatterns = [
    path('reservations/<int:id>/rooms/', include(router_reservation_rooms.urls)),
    path('reservations/', include(router_reservations.urls)),
]
