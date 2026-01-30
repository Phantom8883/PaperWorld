## Slug generation (IMPORTANT) views

Текущая реализация учебная.

Почему:
- проект маленький
- нет нагрузки
- важно понять механику

Риски:
- много запросов при спаме
- race condition

Как делать в проде:
- unique constraint в БД
- try/except IntegrityError
- rate limiting
- captcha
- auth-only доступ
