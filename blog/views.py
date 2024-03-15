from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'ABC',
        'title': "Blog Post 1",
        'content': "contentttt",
        'date_posted': "August 28, 2011"
    },
    {
        'author': 'XYZ',
        'title': "Blog Post 2",
        'content': "tttt",
        'date_posted': "August 29, 2011"
    },
]

def home(request):
    template_name = 'blog/home.html'
    context = {
        'posts': posts
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'blog/about.html'
    context = {
        'title': 'About'
    }
    return render(request, template_name, context)
