from django.urls import path, include
from hotels.views.dicts import (AccommodationTypeView,
                                AccommodationTypeHotelsView,
                                AccommodationTypeSearchView)
from rest_framework.routers import DefaultRouter
from hotels.views.hotels import HotelView
from hotels.views.rooms import HotelRoomView


router_hotels = DefaultRouter()
router_rooms = DefaultRouter()
router_accommodation_type = DefaultRouter()

router_hotels.register(r'', HotelView, 'hotels')
router_rooms.register(r'', HotelRoomView, 'rooms')
router_accommodation_type.register(r'', AccommodationTypeHotelsView,
                                   'accommodation_types_hotels')

urlpatterns = [
    path('dicts/accommodation-types/search/',
         AccommodationTypeSearchView.as_view(),
         name='accommodation_types_search'),
    path('dicts/accommodation-types/', AccommodationTypeView.as_view(),
         name='accommodation_types'),
    path('hotels/dicts/accommodation-types/',
         include(router_accommodation_type.urls)),
    path('hotels/<int:id>/rooms/', include(router_rooms.urls)),
    path('hotels/', include(router_hotels.urls)),
]
