from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from datetime import datetime

# Create your views here.
def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/index.html', context)

def newpost(request):
    if request.method == 'POST':
        Post.objects.create(post=request.POST['post'])
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/posts_index.html', context)

def delete(request, number):
    Post.objects.get(id = number).delete()
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/posts_index.html', context)