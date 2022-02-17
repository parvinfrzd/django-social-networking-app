from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import CommentForm

from main_app.models import Post, Comment

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
    print("in show")
    post = Post.objects.get(id=post_id)
    comment_form = CommentForm()
    return render(request, 'show.html', {'post': post, 'comment_form': comment_form})

def add_comment(request, post_id):
  print("in add_comment")
	# create the ModelForm using the data in request.POST
  form = CommentForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_comment = form.save(commit=False)
    new_comment.post_id = post_id
    new_comment.save()
  return redirect('show', post_id=post_id)

def delete_comment(request, post_id, comment_id):
  Comment.objects.get(id=comment_id).delete()
  return redirect('show', post_id=post_id)

def index(request):
  return redirect('/posts')