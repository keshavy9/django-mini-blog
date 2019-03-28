from django.shortcuts import render
from django.views import generic
from .models import Blog, Blogger

# Create your views here.

def index():
    pass

class BlogListView(generic.ListView):
    model = Blog

class BlogDetailView(generic.DetailView):
    model = Blog

class BloggerListView(generic.ListView):
    model = Blogger

class BloggerDetailView(generic.DetailView):
    model = Blogger        

