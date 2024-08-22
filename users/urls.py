from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views.users import (
    UserView,
    MeUserView,
)

router_users = DefaultRouter()
router_users.register(r'', UserView, 'users')

urlpatterns = [
    path('users/', include(router_users.urls)),
    path('users/me/', MeUserView.as_view(), name='me'),
]
