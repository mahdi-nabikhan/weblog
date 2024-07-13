from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from blog.models import Post
from .models import Profile

# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect('blog:index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog:index')

    return render(request, template_name='forms/login_form.html')


def user_logout(request):
    logout(request)
    return redirect('blog:index')


def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            user = User(username=username, email=email, password=password)
            user.set_password(password)
            user.save()
            return redirect('blog:index')
        else:
            return
    return render(request, template_name='forms/registeration.html')


def profile(request):
    profile = Profile.objects.get(user__id=request.user.id)
    post = Post.objects.filter(author=profile.user)
    context = {'user': profile, 'post': post}
    return render(request, 'accounts/profile.html', context)
