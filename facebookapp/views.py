from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth import login ,authenticate
from .models import Profilemodel,Post,comment


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(profileuser__followers=request.user)
        profile = Profilemodel.objects.get(user=request.user)
        friends = profile.followers.all()
        # print(friends)
        # print(profile)

        return render(request, 'index.html',{'posts':posts,'friends':friends})
    else :
        return redirect('login')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        # print(username)
        if user is not None:
            auth.login(request,user)

            return redirect('/')
        else :
            messages.info(request,"invalid credentials")
            return redirect('login')

    else :
        return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']


        if User.objects.filter(username = username).exists():
            messages.info(request, "username taken")
            return redirect('register')
        elif User.objects.filter(email = email).exists():
            messages.info(request, "email taken")
            return redirect('register')
        else :
            user = User.objects.create_user(username=username,
                                            password=password, email=email, first_name= firstname, last_name = lastname)
            # print(user)
            user.save()
            if user :
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request, user)
                    return redirect('updateProfile')
            # return render(request,'updateProfile.html')

    else :
        return render(request, 'register.html')

def logout(request):


    auth.logout(request)
    return redirect('login')

def updateProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            bio = request.POST['bio']
            profilepic = request.FILES['profilepic']
            nickname = request.POST['nickname']
            profiles = Profilemodel.objects.create(user=request.user,image=profilepic,bio=bio,nickname=nickname)
            return redirect('profile')
        else:
            return render(request,'profileUpload.html')
    else :
        return redirect('login')



def profile(request):
    if request.user.is_authenticated:
        profile = Profilemodel.objects.get(user=request.user)
        friends = profile.followers.all()
        posts = Post.objects.filter(profileuser=profile).order_by('-time')

        print(profile)

        return render(request,'profile.html',{'profiles': profile,'posts':posts,'friends':friends})
    else :
        return redirect('login')


def friends(request):
    if request.user.is_authenticated:
        profile = Profilemodel.objects.get(user=request.user)
        friends = profile.followers.all()
        all=Profilemodel.objects.all()
        # print(friends,"ok")
        # print(all)
        return render(request, 'friends.html',{'friends' : friends, 'all':all})
    else :
        return redirect('login')




def updatePost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            profile = Profilemodel.objects.get(user=request.user)
            postdesc = request.POST['desc']
            file = request.FILES['image']
            # print(file)
            posts = Post.objects.create(postImg=file,profileuser=profile,user=request.user,text=postdesc)
            return render(request,'profile.html')
        else:
            messages.info(request, "something went wrong")
            return render(request,'uploadPost.html')
    else:
        return redirect('login')


def likePost(request,id):
    print(request.method)
    if request.method == 'POST':
        postid = id
        post = Post.objects.get(id=postid)
        post.likes.add(request.user)
        return redirect("/")

def search(request):
    if request.method == 'GET':
        search = request.GET['search1']


        user = Profilemodel.objects.filter(user__username__icontains=search)

        return render(request,'search.html',{'all':user})
    else :
        return redirect('/')


def follow(request):
    if request.method == 'POST':

        userfollow = request.POST['user']
        user = User.objects.get(username=userfollow)
        activeuser = User.objects.get(username=request.user)
        followingmodel = Profilemodel.objects.get(user=activeuser)

        followmodel = Profilemodel.objects.get(user=user)

        followingmodel.following.add(user)
        followmodel.followers.add(request.user)

        return redirect('friends')
    else :

        return redirect("friends")


def notfound(request,exception):
    return render(request, 'error.html')



def comments(request,id):
    print(request.method,id)
    if request.method == 'POST':
        postid = id
        posts = Post.objects.get(id= postid)
        print(posts)
        # posts = Post.objects.filter(id=postid)
        # print(posts)
        comments10 = comment.objects.filter(post=id,parent=None).order_by('-time')
        print(comments10)
        replies= comment.objects.filter(post=id).exclude(parent=None)
        print(replies)
        replyDict={}
        for reply in replies:
            if reply.parent.id not in replyDict.keys():
                replyDict[reply.parent.id]=[reply]
            else:
                replyDict[reply.parent.id].append(reply)
        return render(request, 'comments.html',{'posts':posts,'comments':comments10 ,'replyDict': replyDict})


def postComment(request):
    if request.method == "POST":
        comment1=request.POST.get('comment')
        user = request.user
        postid =request.POST.get('postid')
        print(postid)
        post= Post.objects.get(id=postid)
        parentid = request.POST.get('parentid')

        print(parentid)
        # comments=comment.objects.create(comment= comments, user=request.user, post=post)
        if parentid== None:
            comments=comment.objects.create(comment1= comment1, user=request.user, post=post)
            return redirect('/')
        else:
            parent= comment.objects.get(id=parentid)
            comments=comment.objects.create(comment1= comment1, user=user, post=post , parent=parent)

            return redirect('/')
