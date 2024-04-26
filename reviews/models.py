from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True,
            'null': True,
            }


class Review(models.Model):
    """Создаем модель отзыва"""
    text = models.TextField(verbose_name='Текст отзыва', **NULLABLE)
    author = models.ForeignKey(verbose_name='Автор отзыва', on_delete=models.CASCADE, **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now(), verbose_name='дата отзыва')

    def __str__(self):
        return f'{self.author}'

    class Meta:
        class Meta:
            verbose_name = 'объявление'
            verbose_name_plural = 'объявления'
