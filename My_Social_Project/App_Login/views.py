from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from App_Login.forms import CreateNewUser,LoginForm,EditProfile
from django.contrib.auth.models import User
from App_Login.models import UserProfile,Follow
from django.contrib.auth.forms import AuthenticationForm 
from App_Posts.forms import PostForm
# Create your views here.

def sign_up(request):
    form = CreateNewUser
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user) 
            user_profile.save()
            return HttpResponseRedirect(reverse('app_login:login'))
    return render(request,'App_Login/sign_up.html',context={'title':' Sign up . Instagram','form':form,'register':registered})


def login_page(request):
    form = LoginForm() 
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('app_posts:home'))
    return render(request,'App_Login/login_page.html',context={'title':"Login",'form':form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('app_login:login'))


@login_required
def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)
    if request.method == 'POST':
        form = EditProfile(request.POST,request.FILES,instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            # form=UserProfile(instance=current_user)
            return HttpResponseRedirect(reverse('app_login:profile'))
    return render(request,'App_Login/edit_profile.html',context={'form':form,'title':"Edit Profile"})


@login_required 
def profile(request):
    form = PostForm()
    if request.method == 'POST': 
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('app_login:profile'))
    return render(request,'App_Login/user.html',context={'form':form}) 

@login_required
def other_user(request,username):
    user_other = User.objects.get(username=username)
    already_followed = Follow.objects.filter(following =user_other,follower=request.user)
    if user_other == request.user:
        return HttpResponseRedirect(reverse('app_login:profile'))
    return render(request,'App_Login/other_user.html',context={'user_other':user_other,'already_followed':already_followed})


@login_required
def follow(request,username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(following=following_user,follower=follower_user)
    if not already_followed:
        followed = Follow(following=following_user,follower=follower_user)
        followed.save()
    return HttpResponseRedirect(reverse('app_login:other_user', kwargs={'username':username}))

def unfollow(request,username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(following=following_user,follower=follower_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('app_login:other_user', kwargs={'username':username}))

