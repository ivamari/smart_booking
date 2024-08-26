from django.urls import path, include
from hotels.views.dicts import AccommodationTypeView
from rest_framework.routers import DefaultRouter
from hotels.views.hotels import HotelView

router_hotels = DefaultRouter()
router_hotels.register(r'', HotelView, 'hotels')

urlpatterns = [
    path('dicts/accommodation-types/', AccommodationTypeView.as_view(),
         name='accommodation_types'),
    path('hotels/', include(router_hotels.urls)),
]
