from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# posts = [
#     {
#         'author': 'Aniket Kumar',
#         'title': 'Blog Post 1',
#         'content': 'First Post Content',
#         'date_posted': 'Dec 23, 2024'
#     },
#     {
#         'author': 'Kartik',
#         'title': 'Blog Post 2',
#         'content': 'Second Post Content',
#         'date_posted': 'Dec 24, 2024'
#     }
#
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

