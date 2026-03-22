from django.contrib import admin
from .models import Palete

@admin.register(Palete)
class PaleteAdmin(admin.ModelAdmin):
    list_display = ("name", "number_of_colors", "favourited", "viewed")
    list_filter = ("viewed", "favourited")
    search_fields = ("name",)
