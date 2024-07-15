from django.shortcuts import render

from blog.models import *


# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts, 'resent': posts[0:3]}
    return render(request, template_name='index.html', context=context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request=request, template_name='post-details.html', context=context)


def all_posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request=request, template_name='post-list.html', context=context)


def category_detail(request, pk=None):
    category = Category.objects.get(pk=pk)
    post = Post.objects.filter(category=category)
    context = {'posts': post}
    return render(request, template_name='category_post.html', context=context)
