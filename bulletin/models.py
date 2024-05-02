from django.db import models

from users.models import User

NULLABLE = {'blank': True,
            'null': True,
            }


class Bulletin(models.Model):
    """Создаем модель объявления"""

    title = models.CharField(max_length=100, verbose_name='Название товара', **NULLABLE)
    price = models.IntegerField(verbose_name='Цена товара', **NULLABLE)
    description = models.TextField(verbose_name='Описание товара', **NULLABLE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата объявления')

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
