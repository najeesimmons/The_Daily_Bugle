from ast import Del
import imp
from unicodedata import name
from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView # <- a class to use files in templates directory as views
from .models import Freak # MUST IMPORT IN ORDER TO PASS MODELS TO VIEWS
from .models import Article # MUST IMPORT IN ORDER TO PASS MODELS TO VIEWS
from .models import Writer # MUST IMPORT IN ORDER TO PASS MODELS TO VIEWS
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse


# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class FreakList(TemplateView):
    template_name = "freak_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["freaks"] = Freak.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["freaks"] = Freak.objects.all()
            context["header"] = "Freaks of New York City"
        return context

class FreakCreate(CreateView):
    model = Freak
    fields = ['name', 'allegiance', 'bio', 'species', 'image',]
    template_name = "freak_create.html"
    success_url = "/freaks/"

class FreakDetail(DetailView):
    model = Freak
    template_name = "freak_detail.html"

class FreakUpdate(UpdateView):
    model = Freak
    fields = ['name', 'allegiance', 'bio', 'species', 'image',]
    template_name = "freak_create.html"
    
    def get_success_url(self):
        return reverse('freak_detail', kwargs={'pk': self.object.pk})

class FreakDelete(DeleteView):
    model = Freak
    template_name = "freak_delete_confirmation.html"
    success_url = "/freaks"

class ArticleList(TemplateView):
    template_name = "article_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        headline = self.request.GET.get("headline")
        # If a query exists we will filter by name 
        if headline != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["articles"] = Article.objects.filter(headline__icontains=headline)
            context["header"] = f"Searching for {headline}"
        else:
            context["articles"] = Article.objects.all()
            context["header"] = "Trending Articles"
        return context

class ArticleCreate(CreateView):
    model = Article
    freak = Freak
    fields = ['headline', 'author', 'body', 'image', 'freak']
    template_name = "article_create.html"
    success_url = "/articles/"

class ArticleDetail(DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleUpdate(UpdateView):
    model = Article
    freak = Freak
    fields = ['headline', 'author', 'body', 'image', 'freak']
    template_name = "article_update.html"
    success_url = "/articles/"

class ArticleDelete(DeleteView):
    model = Article
    template_name = "article_delete_confirmation.html"
    success_url = "/articles"

class WriterList(TemplateView):
    template_name = "writer_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["writers"] = Writer.objects.filter(name__icontains=name)
            context["name"] = f"Searching for {name}"
        else:
            context["writers"] = Writer.objects.all()
            context["header"] = "Our Team"
        return context