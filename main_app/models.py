from email.mime import image
from email.policy import default
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

class Article(models.Model):

    headline = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    body = models.TextField(max_length=1000)
    image = models.CharField(max_length=500, default = "https://static.wikia.nocookie.net/marveldatabase/images/9/99/Daily_Bugle_%28Earth-1048%29_from_Marvel%27s_Spider-Man_%28video_game%29_001.jpg/revision/latest?cb=20180930035134")
    freak = models.ForeignKey(
        Freak, on_delete=models.CASCADE, related_name="articles")
    
    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']

class Writer(models.Model):

    name = models.CharField(max_length=100) 
    bio = models.TextField(max_length=500)
    image = models.CharField(max_length=500)