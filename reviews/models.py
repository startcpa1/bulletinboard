from django.db import models

from bulletin.models import Bulletin
from users.models import User

NULLABLE = {'blank': True,
            'null': True,
            }


class Review(models.Model):
    """Создаем модель отзыва"""
    text = models.TextField(verbose_name='Текст отзыва', **NULLABLE)
    author = models.ForeignKey(User, verbose_name='Автор отзыва', on_delete=models.DO_NOTHING, **NULLABLE)
    bulletin = models.ForeignKey(Bulletin, verbose_name='Объявление', on_delete=models.CASCADE, **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата отзыва')

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
        ordering = ('-created_at',)
