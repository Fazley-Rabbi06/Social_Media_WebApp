from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from App_Login.models import Follow
from App_Posts.models import Post,Like
# Create your views here.
@login_required
def home(request):
    following_list = Follow.objects.filter(follower=request.user)
    posts = Post.objects.filter(author__in=following_list.values_list('following'))
    liked_post = Like.objects.filter(user=request.user)
    liked_post_list=liked_post.values_list('post',flat=True)
    if request.method == 'GET':
        search = request.GET.get('search','')
        result = User.objects.filter(username__icontains=search) 
    return render(request,'App_Posts/home.html',context={'title':"Homepage",'search':search,'result':result,'posts':posts,'liked_post_list':liked_post_list})    

@login_required
def like(request,pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post,user=request.user)
    if not already_liked:
        liked = Like(post=post,user=request.user)
        liked.save()
    return HttpResponseRedirect(reverse('app_posts:home'))

@login_required
def unlike(request,pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post,user=request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('app_posts:home'))
