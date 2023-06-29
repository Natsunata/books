from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    books = models.ManyToManyField('booksapp.Book', related_name="books")
    commentsnum = models.PositiveSmallIntegerField(default=0)
    booksnum = models.PositiveSmallIntegerField(default=0)
    




