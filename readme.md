# Проект "Бэкенд доски объявлений"

## Описание проекта

Проект представляет собой бэкенд для доски объявлений, где авторизованный пользователь может создавать, редактировать и удалять объявления, а также оставлять отзывы под каждым объявлением. Также пользователь имеет возможность осуществлять поиск по заголовкам объявлений.

## Функциональность

### Доступные действия для пользователей

- **Для анонимного пользователя**:
  - Просмотр всех объявлений.

- **Для авторизованного пользователя**:
  - Просмотр объявления.
  - Создание объявления.
  - Редактирование своего объявления.
  - Удаление своего объявления.
  - Оставление отзывов.

- **Для администратора**:
  - Просмотр всех объявлений.
  - Создание, редактирование и удаление объявлений.
  - Управление отзывами.

## Пагинация

Для удобства просмотра объявлений реализована пагинация с выводом по 4 объявления на странице.

## Безопасность

Для обеспечения безопасности вашего сервера, настройте CORS.

## Стек технологий

Проект реализован с использованием следующего стека технологий:
- Django
- PostgreSQL
- ORM
- Docker
- Docker-compose

## Инструкция по запуску проекта

1. Убедитесь, что у вас установлен Docker и Docker Compose.
2. Клонируйте репозиторий и перейдите в его директорию.
3. Выполните следующие команды:
   ```bash
   docker-compose build
   docker-compose up
   docker-compose exec web python manage.py csu
