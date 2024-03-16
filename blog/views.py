from django.shortcuts import render
from .models import Post

def home(request):
    template_name = 'blog/home.html'
    context = {
        'posts': Post.objects.all()
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'blog/about.html'
    context = {
        'title': 'About'
    }
    return render(request, template_name, context)
