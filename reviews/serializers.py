from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from bulletin.models import Bulletin
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для отзывов"""
    class Meta:
        model = Review
        fields = '__all__'
