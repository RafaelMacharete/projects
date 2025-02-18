from django.db import models

class Book(models.Model):
    book_title = models.CharField(max_length=50)
    book_author = models.CharField(max_length=60)
    book_genre = models.CharField(max_length=40)