from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
posts = [
    {
        'author': 'Dennis Dadey',
        'title': 'Myself',
        'content': 'This is the first post that describes who I am\nI am the Dee',
        'date_posted': 'February 17, 2023'
    },
    {
        'author': 'Henrietta',
        'title': 'Kumasi Nyonko',
        'content': 'Kumasi, also known as the garden city is a beautiful tropical city',
        'date_posted': 'April 1, 2012'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'story_blog/index.html', context)


def about(request):
    return render(request, 'story_blog/about.html', {'title': 'About'})
