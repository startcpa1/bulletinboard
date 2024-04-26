from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True,
            'null': True,
            }


class Advertisement(models.Model):
    """Создаем модель объявления"""

    title = models.CharField(max_length='100', verbose_name='Название товара', **NULLABLE)
    price = models.IntegerField(verbose_name='Цена товара', **NULLABLE)
    description = models.TextField(verbose_name='Описание товара', **NULLABLE)
    author = models.CharField(verbose_name='Пользователь', **NULLABLE)

    created_at = models.DateTimeField(default=timezone.now(), verbose_name='дата объявления')

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        class Meta:
            verbose_name = 'объявление'
            verbose_name_plural = 'объявления'
