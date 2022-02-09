from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article, Freak, Writer # import the Artist model from models.py
# Register your models here.

admin.site.register(Freak) # this line will add the model to the admin panel
admin.site.register(Article)
admin.site.register(Writer)