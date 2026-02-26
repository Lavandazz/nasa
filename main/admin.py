from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.utils.html import format_html

from main.models import SpaceImage


# Register your models here.


@admin.register(SpaceImage)
class SpaceImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image', 'image_preview')
    search_fields = ('title',)

    def image_preview(self, obj):
        if obj.image:
            return format_html (f'<img src="{obj.image.url}" style="max-height: 100px; max-width: 100px;" />')
        return "Нет изображения"

    image_preview.short_description = 'Превью изображения'

