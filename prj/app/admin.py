from django.contrib import admin
from .models import Palete, Color


@admin.register(Palete)
class PaleteAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "number_of_colors",
        "favourited",
        "viewed"
    )

    list_filter = (
        "viewed",
        "favourited"
    )

    search_fields = ("name",)


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