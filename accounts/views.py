from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *
from blog.models import Post
from .models import Profile


# Create your views here.
def user_login(request):
    if request.user.is_authenticated:
        return redirect('blog:index')
    if request.method == 'POST':
        form = loginForms(data=request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            username = cd.get('username')
            password = cd.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog:index')

    form = loginForms()
    context = {'form': form}
    return render(request, template_name='forms/login_form.html',context=context)


def user_logout(request):
    logout(request)
    return redirect('blog:index')


def user_register(request):
    errors = None
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            age = form.cleaned_data['age']
            phone = form.cleaned_data['phone']
            bio = form.cleaned_data['bio']
            user = User(username=username, email=email, password=password)
            user.set_password(password)
            user.save()

            Profile.objects.create(user=user, age=age, phone_number=phone, bio=bio)
            return redirect('blog:index')
        else:
            form = registerForm(request.POST)
    else:
        form = registerForm()

    context = {'form': form, 'error': errors}
    return render(request, template_name='forms/registeration.html', context=context)


def profile(request):
    profile = Profile.objects.get(user__id=request.user.id)
    post = Post.objects.filter(author=profile.user)
    context = {'user': profile, 'post': post}
    return render(request, 'accounts/profile.html', context)
