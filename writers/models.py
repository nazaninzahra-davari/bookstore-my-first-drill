from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=40)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    pages = models.IntegerField()

