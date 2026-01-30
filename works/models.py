from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class PublishedManager(models.Manager): # Менеджер опубликованных работ
    def get_queryset(self):
        return super().get_queryset().filter(status='PB')  # 'PB' = PUBLISHED


class Work(models.Model):
    class Status(models.TextChoices):
        # не знаю какие статусы нам нужны помимо двух базовых
        DRAFT = 'DF', 'Draft' # черновик (не опубликован)
        PUBLISHED = 'PB', 'Published' # опубликован
        COMPLETED = 'CM', 'Completed' # завершён
        # заморожен


    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish', unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE, # при удалении пользователя, удаляются все фанфики (объекты привязанные к пользователю)
        related_name='works'
    )

    description = models.CharField(max_length=800) # краткое описание фанфика (аннотация)
    # Изменил модель поля на CharField, чтобы у поля были ограничения (было TextField - у него нету ограничений) 
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, # Длина кода статуса в Status - "DF" "PB" "CM" в БД сохраняется по два символа
        choices=Status.choices,
        default=Status.DRAFT
    )
    objects = models.Manager()  # Менеджер по умолчанию
    published = PublishedManager()  # Менеджер для опубликованных работ

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse(
            'works:work_detail', 
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug
                ]
            )