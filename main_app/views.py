from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from main_app.models import Post

class PostList(ListView):
  model = Post

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

