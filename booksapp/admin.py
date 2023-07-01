from django.contrib import admin
from booksapp.models import Book, Comment



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'get_authors', 'commentsnum')

    def get_authors(self, obj):
        return "\n".join([author.full_name for author in obj.authors.all()])
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )





