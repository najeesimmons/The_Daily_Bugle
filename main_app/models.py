from email.mime import image
from unicodedata import name
from django.db import models

# Create your models here.
class Freak(models.Model):

    name = models.CharField(max_length=100)
    allegiance = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    species = models.CharField(max_length=100)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
