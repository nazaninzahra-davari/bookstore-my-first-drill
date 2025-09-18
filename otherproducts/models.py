from django.db import models

# Create your models here.
class Otherproduct(models.Model):
    notebook = models.CharField(max_length=50)
    pencil = models.CharField(max_length=50)
    flashcard = models.CharField(max_length=50)

