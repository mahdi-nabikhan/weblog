from django.shortcuts import render

from blog.models import Post


# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request ,template_name='index.html',context=context)