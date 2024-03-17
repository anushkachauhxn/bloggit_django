from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


def home(request):
    template_name = 'blog/home.html'
    context = {
        'posts': Post.objects.all()
    }
    return render(request, template_name, context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


def about(request):
    template_name = 'blog/about.html'
    context = {
        'title': 'About'
    }
    return render(request, template_name, context)
