from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from rest_framework import generics
from rest_framework.response import Response

from .models import *
from .forms import *
from Api.serializers import *

# Create your views here.

def loginView(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('Base:home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = get_object_or_404(User, email=email)
        except:
            messages.error(request, 'user does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('Base:home')
        else:
            messages.error(request, 'Username OR password does not exist')

    context = {'page': page}
    return render(request, 'Base/login_register.html', context)


# =======================================================================================================================================================

def registerView(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('Base:home')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {'form': form}
    return render(request, 'Base/login_register.html', context)


# =======================================================================================================================================================

def userDetailView(request):
    pk = request.user.id
    user = User.objects.get(id=pk)
    articles = user.article_set.all()

    context = {'user': user, 'articles': articles}
    return render(request, 'Base/user_detail.html', context)


# =======================================================================================================================================================

@login_required(login_url='login')
def updateUserView(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('Base:user-detail')

    context = {'form': form}
    return render(request, 'Base/update_user.html', context)


# =======================================================================================================================================================

@login_required(login_url=login)
def deleteUserView(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        return redirect('Base:home')

    return render(request, 'Base/confirm_delete.html')


# =======================================================================================================================================================

def logoutView(request):
    logout(request)
    return redirect('Base:home')


# =======================================================================================================================================================

def home(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    articles = Article.objects.filter(
        Q(category__name__icontains=q) |
        Q(owner__name__icontains=q) |
        Q(title__icontains=q) |
        Q(body__icontains=q)
    )

    context = {'articles': articles}
    return render(request, 'Base/home.html', context)


# =======================================================================================================================================================

@login_required(login_url='Base:login')
def articleCreateView(request):
    form = ArticleForm()
    categories = Category.objects.all()

    if request.method == 'POST':
        category_name = request.POST.get('category')
        category, created = Category.objects.get_or_create(name=category_name)
        Article.objects.create(
            owner=request.user,
            category=category,
            title=request.POST.get('title'),
            body=request.POST.get('body')
        )
        return redirect('Base:home')

    context = {'form': form, 'categories': categories}
    return render(request, 'Base/create.html', context)


# =======================================================================================================================================================

def articleDetailView(request, pk):
    article = get_object_or_404(Article, id=pk)

    context = {'article': article}
    return render(request, 'Base/article_detail.html', context)


# =======================================================================================================================================================

@login_required(login_url='Base:login')
def articleUpdateView(request, pk):
    article = get_object_or_404(Article, id=pk)
    form = ArticleForm(instance=article)
    categories = Category.objects.all()

    if request.user != article.owner:
        return HttpResponse('Only the owner of this article can alter/edit it...')

    if request.method == 'POST':
        category_name = request.POST.get('category')
        category, created = Category.objects.get_or_create(name=category_name)
        article.category = category
        article.title = request.POST.get('title')
        article.body = request.POST.get('body')
        article.save()
        return redirect('Base:home')

    context = {'article': article, 'form': form, 'categories': categories}
    return render(request, 'Base/article_update.html', context)


# =======================================================================================================================================================

@login_required(login_url='Base/login')
def articleDeleteView(request, pk):
    article = get_object_or_404(Article, id=pk)

    if request.user != article.owner:
        return HttpResponse('Only the owner of this article can delete it...')

    if request.method == 'POST':
        article.delete()
        return redirect('Base:home')

    context = {'article': article}
    return render(request, 'Base/delete.html', context)



