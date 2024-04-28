from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny

from bulletin.models import Bulletin
from bulletin.serializers import BulletinSerializer
from users.permissions import IsAdmin, IsOwner


class BulletinViewSet(viewsets.ModelViewSet):
    """Описание функциональности:
    - `list`: Просмотр всех объявлений (разрешено без аутентификации)
    - `retrieve`: Получение отдельного объявления (требуется аутентификация)
    - `create`: Создание нового объявления (требуется аутентификация)
    - `update`: Обновление объявления (доступно только администратору или автору)
    - `destroy`: Удаление объявления (доступно только администратору или автору)

    Права доступа:
    - `list`: Доступно всем пользователям
    - `retrieve`: Только аутентифицированным пользователям
    - `create`: Только аутентифицированным пользователям
    - `update`: Только администратору или автору объявления
    - `destroy`: Только администратору или автору объявления"""

    serializer_class = BulletinSerializer
    queryset = Bulletin.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('author',)
    search_fields = ('title',)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'list':
            self.permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'update':
            self.permission_classes = [IsAdmin, IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [IsAdmin, IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        new_ads = serializer.save()
        new_ads.author = self.request.user
        new_ads.save()
