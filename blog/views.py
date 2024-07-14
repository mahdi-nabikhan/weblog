from django.shortcuts import render

from blog.models import Post


# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, template_name='index.html', context=context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request=request, template_name='post-details.html', context=context)
