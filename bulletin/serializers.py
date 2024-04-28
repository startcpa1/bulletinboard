from rest_framework import serializers
from bulletin.models import Bulletin


class BulletinSerializer(serializers.ModelSerializer):
    """Сериализатор для объявлений"""
    class Meta:
        model = Bulletin
        fields = '__all__'
