from django.contrib import admin
from .models import Book
from .forms import BookForm

class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ['title', 'authors', 'genre', 'publisher', 'publication_date', 'language', 'price', 'format']
    search_fields = ['title', 'authors', 'genre', 'publisher']
    list_filter = ['genre', 'language', 'publisher']

# Register the model in admin
admin.site.register(Book, BookAdmin)
