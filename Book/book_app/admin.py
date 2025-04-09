from django.contrib import admin
from .models import book_app
from .forms import bookForm
# Register your models here.

@admin.register(book_app)
class bookAdmin(admin.ModelAdmin):
    list_display = ('book_name','book_genre')
    search_fields = ('book_name','book_genre')
    list_filter = ('book_genre',)