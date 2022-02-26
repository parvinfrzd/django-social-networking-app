# PARJALAN

#### Parjalan is an ongoing replica of social media platforms developed as a part of General Assembly SEI program. 
<br>

## Table of Content: 

1. [Getting Started](#getting-started)
2. [Getting Started (dev)](#getting-started-(dev))
3. [Project Management](#project-management)
4. [Entity Relationship Diagram](#entity-relationship-diagram)
5. [User Stories and Wireframe](#user-stories-and-wireframe)
6. [Code Snippets](#code-snippets)
7. [Gallery](#gallery)
8. [Technologies](#technologies)
9. [Future Updates](#future-updates)
10. [References](#references)
   <br>
##  Getting Started:
#### To get started with your first post, click on this [link](https://parjalan.herokuapp.com).
<br>

## Getting Started (dev): 
#### You can either fork this repository, or contribute to the project. Please refer to the Wiki page for code of conduct. If you are interested in what we do, give us a star.

## Project Management: 
#### For more info on the project please visit our [Trello board](https://trello.com/b/k5oNpVFw/djanjo-data-warriors-project-3)
#### Roles: 
 1. [Parvin Farahzadeh](): Github Manager, Back-end developer, System design
 2. [Jas Rai](): Full-stack developer, Trello board manager, and front-end development
 3. [Dylan Burston](): Full-stack developer

## Entity Relationship Diagram: 
#### Our ERD is based on the user stories we defined for the first MVP
<br>

![alt text](https://github.com/parvinfrzd/django-social-networking-app/blob/master/main_app/static/images/readme_img/erd.png?raw=true)

<br>

## User Stories and Wireframe: 
#### AAU I want to be able to log in / log out, or sign up as a user 
#### AAU I want to be able to make a unique profile to myself 
#### AAU I want to be able to read, update my profile 
#### AAU I want to be able to view profiles other that my own
#### AAU I want to be able follow/unfollow as many user profiles as I want 
#### AAU I want to be able to post on the social media application 
#### AAU I want to be able to comment on my post, as well as other people posts 
#### AAU I want to be able to see my following accounts post 
#### AAU I want to be able to be able to like/dislike other users posts 
#### AAU I want to be the only user to be able to update and delete my posts 
#### AAU I want to be able to delete other user's comments on my posts 
<br>

![alt text](https://github.com/parvinfrzd/django-social-networking-app/blob/master/main_app/static/images/readme_img/wireframe.png?raw=true)
<br>

## Code Snippets: 
As a group, we used different methods to tackle our problems 

1. Make the follow/unfollow relation among users: 
```
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
```
   2. For update and delete, we decided to go with View class in Django : 
```
class ProfileDelete(LoginRequiredMixin,DeleteView):
    model = Profile
    success_url = '/'
    def delete(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        profile = Profile.objects.filter(profile_id=id)
        logout(request,self.user)
        profile.delete()
        return HttpResponseRedirect(reverse(''))
```
   3. The like and dislike functionality on user posts required both class based and costume methods: 
```
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
```
## Gallery: 
![alt text](https://github.com/parvinfrzd/django-social-networking-app/blob/master/main_app/static/images/readme_img/1.png?raw=true)
![alt text](https://github.com/parvinfrzd/django-social-networking-app/blob/master/main_app/static/images/readme_img/2.png?raw=true)
![alt text](https://github.com/parvinfrzd/django-social-networking-app/blob/master/main_app/static/images/readme_img/3.png?raw=true)
![alt text](https://github.com/parvinfrzd/django-social-networking-app/blob/master/main_app/static/images/readme_img/4.png?raw=true)
![alt text](https://github.com/parvinfrzd/django-social-networking-app/blob/master/main_app/static/images/readme_img/5.png?raw=true)
![alt text](https://github.com/parvinfrzd/django-social-networking-app/blob/master/main_app/static/images/readme_img/6.png?raw=true)
![alt text](https://github.com/parvinfrzd/django-social-networking-app/blob/master/main_app/static/images/readme_img/7.png?raw=true)
![alt text](https://github.com/parvinfrzd/django-social-networking-app/blob/master/main_app/static/images/readme_img/8.png?raw=true)

## Technologies: 

<a href="https://cdnlogo.com/logo/python_358.html"><img src="https://cdn.cdnlogo.com/logos/p/3/python.svg" width="50"></a>
<br>

<a href="https://cdnlogo.com/logo/django_41269.html"><img src="https://cdn.cdnlogo.com/logos/d/97/django-community.svg" width="50"></a>
<br>

<a href="https://cdnlogo.com/logo/postgresql_39744.html"><img src="https://cdn.cdnlogo.com/logos/p/93/postgresql.svg" width="50"></a>
<br>

## Future Updates: 

1. Add a more slick user flow 
2. Add hashtag and search bar for an easier access to posts, and profiles
2. Add features like market place and groups

## References: 
#### We recommend you to checkout these two tutorials on the basis of building social media applications with Django and Python 
1. [Legion Script](https://www.youtube.com/channel/UCF7k5gX55WvJ-SFXGsPsLTg): A good resource for building any trending django based application.
2. [RealPython](https://realpython.com/): A website full of python tutorials.

