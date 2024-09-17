from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reservations.views.reservations import ReservationView

router_reservations = DefaultRouter()

router_reservations.register(r'', ReservationView, 'reservations')

urlpatterns = [
    path('reservations/', include(router_reservations.urls)),
]
