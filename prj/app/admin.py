from django.contrib import admin
from .models import Book, Writter
from .models import Palete

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating']

@admin.register(Writter)
class WritterAdmin(admin.ModelAdmin):
    pass

@admin.register(Palete)
class Palete_Admin(admin.Palete_Admin):
    pass
