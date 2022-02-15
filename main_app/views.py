from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

def dashboard(request):
    return render(request, "base.html")

def about(request):
    return render(request, "about.html")

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'main_app/profile_list.html', {'profiles':profiles})

def profile(request,pk): 
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request,'main_app/profile.html',{'profile':profile})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
    
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = SignUpForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
