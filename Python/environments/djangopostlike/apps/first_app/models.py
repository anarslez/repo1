from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<User object: {} {} {}>".format(self.first_name, self.last_name, self.email)
class Post(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    uploader = models.ForeignKey(User, related_name = 'uploaded_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Post object: {} {} {}>".format(self.name, self.desc, self.uploader)
class Like(models.Model):
    post = models.ForeignKey(Post,related_name = 'liked_by')
    user = models.ForeignKey(User, related_name = 'liked_post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Like object: {} {}>".format(self.post, self.user)