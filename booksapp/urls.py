from django.urls import  path
from booksapp.views import AuthorsListView, BooksListView, AuthorsPageListView

app_name = 'booksapp'


urlpatterns = [
    path('books/', BooksListView.as_view(), name='books'),
    path('authors/', AuthorsListView.as_view(), name='authors'),
    path('authors/authorspage/<int:author_id>', AuthorsPageListView.as_view(), name='authorspage'),

]