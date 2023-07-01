from django.shortcuts import render
from django.views.generic.base import TemplateView
from common.views import TitleMixin
from booksapp.models import Book
from authorsapp.models import Author
from django.views.generic.list import ListView


def home(request):
    return render(request, 'booksapp/home.html')

class AuthorsListView(TitleMixin, ListView):
    model = Author
    template_name = 'booksapp/authors.html'
    paginate_by = 3
    title = 'Books - Авторы'

    
    
class BooksListView(TitleMixin, ListView):
    model = Book
    template_name = 'booksapp/books.html'
    paginate_by = 3
    title = 'Books - Books'


class AuthorsPageListView(TitleMixin, ListView):
    model = Book
    template_name = 'booksapp/authorspage.html'
    paginate_by = 3
    title = 'Books - Страница Автора'

    def post(request):
        context = {
            'posts': Book.objects.filter(author=request.user)
        }

        return render(request, 'index.html', context)

    