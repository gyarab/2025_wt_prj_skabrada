from django.contrib import admin
from .models import Book, Writter

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating']

@admin.register(Writter)
class WritterAdmin(admin.ModelAdmin):
    pass

