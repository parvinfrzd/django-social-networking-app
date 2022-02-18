from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Profile, Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .forms import SignUpForm, CommentForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def dashboard(request):
    return render(request, "base.html")

def about(request):
    return render(request, "about.html")

@login_required
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'main_app/profile_list.html', {'profiles':profiles})

@login_required
def profile(request,pk): 
    profile = Profile.objects.get(pk=pk)
    current_user = request.user.profile

    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if(current_user.pk != profile.pk):
            if action == "follow":
                current_user_profile.follows.add(profile)
            elif action == "unfollow":
                current_user_profile.follows.remove(profile)
            current_user_profile.save()
    return render(request,'main_app/profile.html',{'profile':profile, 'current_user':current_user})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
    
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    form = SignUpForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


<<<<<<< HEAD
=======

>>>>>>> 1753ba04d0888656af559d9d144f88400e185e3f
class ProfileUpdate(LoginRequiredMixin,UpdateView):
    model = Profile
    fields = ['bio','birth_date']

class ProfileDelete(LoginRequiredMixin,DeleteView):
    model = Profile
    success_url = '/'
    def delete(self, request, *args, **kwargs):
        id = self.kwargs['pk']

        profile = Profile.objects.filter(profile_id=id)
        logout(request,self.user)
        profile.delete()
        return HttpResponseRedirect(reverse(''))


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