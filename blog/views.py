from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request,'index.html',context)

def post(request):
    post = Post.objects.get(slug = request.post_slug)
    context = {'post':post}
    return render(request, 'post.html',context)