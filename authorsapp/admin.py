from django.contrib import admin
from authorsapp.models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'booksnum', 'commentsnum')
