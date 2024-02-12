# blog/views.py

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog, Comment
from .forms import SignUpForm, BlogForm, CommentForm
from django.contrib.auth.decorators import login_required

def blog_list(request):
    all_blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': all_blogs})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def home(request):
    user_blogs = Blog.objects.filter(author=request.user)
    return render(request, 'blog/home.html', {'blogs': user_blogs})

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})



def add_comment(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, author=request.user)
    comments = blog.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return redirect('add_comment', blog_id=blog.id)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/add_comment.html', {'blog': blog, 'comments': comments, 'comment_form': comment_form})

@login_required
def edit_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id, author=request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/edit_blog.html', {'form': form, 'blog': blog})

@login_required
def delete_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id, author=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('home')
    return render(request, 'blog/delete_blog.html', {'blog': blog})



