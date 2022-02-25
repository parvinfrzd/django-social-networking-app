from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Profile, Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .forms import SignUpForm, PostForm, CommentForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


@login_required
def dashboard(request):
    users = User.objects.all()
    form = PostForm(request.POST or None)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("social:dashboard")
    form = PostForm()
    posts = Post.objects.order_by('-created_at')
    return render(request, "dashboard.html", {"form": form, "users": users, 'posts': posts})

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
    posts = profile.user.posts.order_by('-created_at')
    form = PostForm(request.POST or None)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect(f"/profile/{profile.pk}")
        
        if(current_user.pk != profile.pk):
            if action == "follow":
                current_user_profile.follows.add(profile)
            elif action == "unfollow":
                current_user_profile.follows.remove(profile)
            current_user_profile.save()
            
    form = PostForm()

    return render(request,'main_app/profile.html',{'profile':profile, 'current_user':current_user, 'posts':posts, 'form': form})

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
    template_name = "main_app/post_list.html"
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        # form = PostForm()

        return render(request, 'main_app/post_list.html', {'post_list': posts})

    def post(self, request, *args, **kwargs):
        post = Post.objects.all()
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/posts/'

class PostUpdate(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['text']
    success_url = '/'

class PostDelete(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/'
    
class CommentUpdate(LoginRequiredMixin,UpdateView):
    model = Comment
    fields = ['text']
    success_url = '/'

class CommentDelete(LoginRequiredMixin,DeleteView):
    model = Comment
    def get_success_url(self):
        post = self.object.post 
        return reverse( 'social:show', kwargs={'post_id': post.id})
    
@login_required
def show(request, post_id):
    current_post_user = Post.objects.get(id=post_id).user
    current_user = request.user
    post = Post.objects.get(id=post_id)

    form = CommentForm(request.POST or None)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect(f"/posts/{post_id}")
    form = CommentForm()
    
    return render(request, 'show.html', {"form": form,'post': post, 'current_post_user':current_post_user, 'current_user': current_user})

class AddLike(View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_dislike = False

        for dislike in post.dislike.all():
            if dislike == request.user:
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

        def likecount():
            print("1")

        likecount()

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
            post.like.remove(request.user)
        
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

