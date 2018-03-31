from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):

    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'articles/index.html', {'posts': posts})

def coming_soon(request):
	return render(request, 'articles/comingsoon.html', {})

def not_found(request):
	return render(request, 'articles/404.html', {})

def confirmation(request):
	return render(request, 'articles/google16ce05cfac0fd7b4.html', {})