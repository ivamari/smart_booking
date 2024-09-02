from drf_spectacular.utils import extend_schema_view, extend_schema
from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from common.views.mixins import LCRUDViewSet
from users.serializers.api.users import (UserListSerializer,
                                         UserRetrieveSerializer,
                                         UserCreateSerializer,
                                         UserUpdateSerializer,
                                         MeUserSerializer)

User = get_user_model()


@extend_schema_view(
    retrieve=extend_schema(summary='Деталка пользователя',
                           tags=['Пользователи']),
    list=extend_schema(summary='Список пользователей', tags=['Пользователи']),
    create=extend_schema(summary='Создать пользователя',
                         tags=['Пользователи']),
    partial_update=extend_schema(summary='Изменить пользователя частично',
                                 tags=['Пользователи']),
    destroy=extend_schema(summary='Удалить пользователя',
                          tags=['Пользователи']),
)
class UserView(LCRUDViewSet):
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    http_method_names = ('get', 'post', 'patch', 'delete',)

    multi_serializer_class = {
        'list': UserListSerializer,
        'retrieve': UserRetrieveSerializer,
        'create': UserCreateSerializer,
        'partial_update': UserUpdateSerializer,
    }


@extend_schema_view(
    get=extend_schema(summary='Профиль пользователя', tags=['Пользователи'])
)
class MeUserView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = MeUserSerializer

    def get_object(self):
        print(self.request.user)
        return self.request.user
