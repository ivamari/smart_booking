from django.urls import path, include

from api.spectacular.urls import urlpatterns as doc_urls
from users.urls import urlpatterns as users_urls
from dicts.urls import urlpatterns as dicts_urls
from clients.urls import urlpatterns as clients_urls
from hotels.urls import urlpatterns as hotels_urls

app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
]
urlpatterns += doc_urls
urlpatterns += users_urls
urlpatterns += dicts_urls
urlpatterns += clients_urls
urlpatterns += hotels_urls

