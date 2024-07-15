from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from blog.models import *
from .forms import *

# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts, 'resent': posts[0:3]}
    return render(request, template_name='index.html', context=context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        body = request.POST['body']
        comments.objects.create(content=body, post=post, author=request.user)

    context = {'post': post}
    return render(request=request, template_name='post-details.html', context=context)


def all_posts(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    pages = request.GET.get('page')
    page_number = paginator.get_page(pages)
    context = {'posts': page_number}
    return render(request=request, template_name='post-list.html', context=context)


def category_detail(request, pk=None):
    category = Category.objects.get(pk=pk)
    post = Post.objects.filter(category=category)
    context = {'posts': post}
    return render(request, template_name='category_post.html', context=context)


def search(request):
    if request.method == 'GET' and 'q' in request.GET:
        query = request.GET['q']
        posts = Post.objects.filter(title__icontains=query)
        context = {'posts': posts}
        return render(request, 'search.html', context)


def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:index')
    context = {'form': form}
    return render(request,template_name='forms/add_post.html', context=context)