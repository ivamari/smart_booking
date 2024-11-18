from django.urls import include, path
from rest_framework.routers import DefaultRouter

from clients.views.clients import ClientView

router_clients = DefaultRouter()
router_clients.register(r'', ClientView, 'users')

urlpatterns = [
    path('clients/', include(router_clients.urls)),
]
