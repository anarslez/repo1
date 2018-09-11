from __future__ import unicode_literals
from django.db import models
from ..first_app.models import User

class MessageManager(models.Manager):
    def message_validator(self, postData):
        errors = {}
        if len(postData['content']) < 1:
            errors["content"] = "Blank messages are not tolerated sir/madam"
        return errors
    def comment_validator(self, postData):
        errors = {}
        if len(postData['content']) < 1:
            errors["content"] = "Blank comments are not tolerated sir/madam"
        return errors

class Message(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, related_name = 'messages')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()
    def __repr__(self):
        return "<Message object: {} {} {}>".format(self.content, self.author, self.created_at)
class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, related_name = 'comments')
    parent = models.ForeignKey(Message, related_name = 'comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MessageManager()
    def __repr__(self):
        return "<Comment object: {} {} {} {}>".format(self.content, self.author, self.parent, self.created_at)