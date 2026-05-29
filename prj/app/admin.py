from django.contrib import admin
from .models import Palette, Color


@admin.register(Palette)
class PaleteAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "number_of_colors",
        "viewed",
    )

    list_filter = (
        "viewed",
    )

    search_fields = ("name",)

    def number_of_colors(self, obj):
        return obj.colors.count()


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "hex_id"
    )

    search_fields = (
        "name",
        "hex_id"
    )