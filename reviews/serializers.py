from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для отзывов"""
    class Meta:
        model = Review
        fields = '__all__'
