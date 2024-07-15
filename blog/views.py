from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from blog.models import *
from .forms import *
from django.views.generic import *


# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts, 'resent': posts[0:3]}
    return render(request, template_name='index.html', context=context)


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.all()
        resent = post[:3]
        context['resent'] = resent
        context['posts'] = post
        return context


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        body = request.POST['body']
        comments.objects.create(content=body, post=post, author=request.user)




class PostDetailView(DetailView):
    template_name = 'post-details.html'
    model = Post

    def post(self, request, *args, **kwargs):
        new = self.get_object()
        print(self.object)
        body = self.request.POST['body']
        comments.objects.create(content=body, author=request.user, post=new)
        return render(request,self.template_name, {'post': new})


def all_posts(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    pages = request.GET.get('page')
    page_number = paginator.get_page(pages)
    context = {'posts': page_number}
    return render(request=request, template_name='post-list.html', context=context)
class AllPostsView(ListView):
    model = Post
    template_name = 'post-list.html'
    context_object_name = 'posts'
    paginate_by = 2


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
    return render(request, template_name='forms/add_post.html', context=context)
