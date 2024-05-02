from rest_framework import generics, status
from rest_framework.response import Response

from users.models import User
from users.permissions import IsProfileUser
from users.serializers import UserSerializer


class UserListView(generics.ListAPIView):
    """Представление информации списка пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """Переопределяем метод для сохранения хешированного пароля"""
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = serializer.data["password"]
        user = User.objects.get(pk=serializer.data["id"])
        user.set_password(password)
        user.is_active = True
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserUpdateView(generics.UpdateAPIView):
    """Представление для обновления информации о пользователе"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsProfileUser]


class UserDetailView(generics.RetrieveAPIView):
    """Представление для получения информации о пользователе"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteView(generics.DestroyAPIView):
    """Представление для удаления информации о пользователе"""
    queryset = User.objects.all()
    permission_classes = [IsProfileUser]
