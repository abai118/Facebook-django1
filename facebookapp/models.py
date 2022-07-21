from django.db import models
from django.contrib.auth.models import User




# Create your models here.


class Profilemodel(models.Model):
    image = models.ImageField(upload_to="ProfilePics")
    bio = models.CharField(max_length=200)
    nickname=models.CharField(max_length=100)
    followers = models.ManyToManyField(User,related_name='followers',blank=True,null=True)
    following  = models.ManyToManyField(User,blank=True,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user")

class Post(models.Model):
    postImg = models.ImageField(upload_to="posts",blank=True,null=True)
    text = models.CharField(max_length=200)
    profileuser = models.ForeignKey(Profilemodel,related_name="profile",on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,related_name="likes",blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, blank=True)

class comment(models.Model):
   
    comment1 = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent =models.ForeignKey('self',on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    
    
    