# Generated by Django 5.0.4 on 2024-04-27 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название товара')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Цена товара')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание товара')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата объявления')),
            ],
            options={
                'verbose_name': 'объявление',
                'verbose_name_plural': 'объявления',
                'ordering': ('-created_at',),
            },
        ),
    ]