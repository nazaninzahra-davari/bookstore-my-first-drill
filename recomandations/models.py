from django.db import models

from booksmenu.models import Book


# Create your models here.
class Recommendation(models.Model):
    isbn = models.CharField(max_length=40)
    pages = models.IntegerField()
    booksrecommended = models.ManyToManyField(Book)
