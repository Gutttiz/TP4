from django.shortcuts import render
from .models import Post
from .forms import CommentForm

def lista_posts(request):
    posts = Post.objects.all()
    form = CommentForm()
    return render(request, "blog/lista_posts.html", {"posts": posts, "form": form})
