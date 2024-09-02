from django.urls import path, include
from hotels.views.dicts import AccommodationTypeView
from rest_framework.routers import DefaultRouter
from hotels.views.hotels import HotelView
from hotels.views.rooms import HotelRoomView

router_hotels = DefaultRouter()
router_rooms = DefaultRouter()
router_hotels.register(r'', HotelView, 'hotels')
router_rooms.register(r'', HotelRoomView, 'rooms')

urlpatterns = [
    path('dicts/accommodation-types/', AccommodationTypeView.as_view(),
         name='accommodation_types'),
    path('hotels/<int:id>/rooms/', include(router_rooms.urls)),
    path('hotels/', include(router_hotels.urls)),
]
