from django.db import models

# Create your models here.
class Sms (models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    pages = models.IntegerField()
    recommenders = models.CharField(max_length=50)



