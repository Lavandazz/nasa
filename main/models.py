from django.db import models

# Create your models here.


# models.py
from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


class SpaceImage(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    image = FilerImageField(
        on_delete=models.CASCADE,
        related_name='slides',
        verbose_name='Изображение',
        null=True,
        blank=True
    )
    # Поле для сортировки. Пакет django-admin-sortable2
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name='Порядок'
    )

    class Meta:
        ordering = ['my_order']  # Сортировка по умолчанию
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    def __str__(self):
        return self.title
