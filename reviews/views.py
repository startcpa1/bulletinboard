from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from reviews.models import Review
from reviews.serializers import ReviewSerializer
from users.permissions import IsOwner


class ReviewListAPIView(generics.ListAPIView):
    """Контроллер просмотра списка отзывов"""
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]


class ReviewCreateAPIView(generics.CreateAPIView):
    """Контроллер создания отзыва"""
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]


class ReviewDetailAPIView(generics.RetrieveAPIView):
    """Контроллер просмотра отзыва"""
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]


class ReviewUpdateAPIView(generics.UpdateAPIView):
    """Контроллер обновления отзыва"""
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class ReviewDeleteAPIView(generics.DestroyAPIView):
    """Контроллер удаление отзыва"""
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
