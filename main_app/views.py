from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View

from main_app.models import Post

def PostList(request):
    post = Post.objects.all()
    print(post)
    return render(request, 'main_app/post_list.html', {'post_list': post})
  
""""
class PostList(ListView):
  post = Post
  def viewposts(self, post, request):
    return post
"""
class PostCreate(CreateView):
  model = Post
  fields = '__all__'
  success_url = '/posts/'

class PostUpdate(UpdateView):
  model = Post
  fields = ['text']
  success_url = '/posts/'

class PostDelete(DeleteView):
  model = Post
  success_url = '/posts/'

def show(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'show.html', {'post': post})

class AddLike(View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_dislike = False

        for dislike in post.dislike.all():
            if dislike == request.user.id:
                is_dislike = True
                break

        if is_dislike:
            post.dislike.remove(request.user)

        is_like = False

        for like in post.like.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.like.add(request.user.id)

        if is_like:
            post.like.remove(request.user.id)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class AddDislike(View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_like = False

        for like in post.like.all():
            if like == request.user:
                is_like = True
                break
        
        if is_like:
            post.like.remove(request.user.id)
        
        is_dislike = False

        for dislike in post.dislike.all():
            if dislike == request.user:
                is_dislike = True
                break
        
        if not is_dislike:
            post.dislike.add(request.user.id)

        if is_dislike:
            post.dislike.remove(request.user.id)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

