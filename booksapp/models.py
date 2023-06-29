from django.db import models



class Book(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    commentsnum = models.PositiveSmallIntegerField(default=0)
    authors = models.ManyToManyField(to='authorsapp.Author', related_name='authors')
 

class Comment(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name='book')
    author = models.ForeignKey(to='authorsapp.Author', on_delete=models.CASCADE, related_name='author')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)


    def __str__(self):
        return self.text
