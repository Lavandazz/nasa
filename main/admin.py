from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from main.models import SpaceImage


# Register your models here.


@admin.register(SpaceImage)
class SpaceImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)


    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 50px; max-width: 50px;" />'
        return "Нет изображения"

