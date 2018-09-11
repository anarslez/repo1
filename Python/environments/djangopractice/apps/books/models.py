from __future__ import unicode_literals
from django.db import models
from ..login.models import User

class BookManager(models.Manager):
    def author_validator(self, postData):
        errors = {}
        if len(postData['name']) < 1:
            errors["name"] = "Name can't be blank"
        if len(Author.objects.filter(name = postData['name'])) > 0:
            errors["name"] = "Author already exists please select author from list"
        return errors
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors["title"] = "Title can't be blank"
        return errors
    def review_validator(self, postData):
        errors = {}
        if len(postData['content']) < 1:
            errors["content"] = "Review can't be blank"
        if postData['rating'].isdigit() == False:
            errors["rating"] = "Rating can't be blank"
        return errors

class Author(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
    def __repr__(self):
        return "<Author object: {}>".format(self.name)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name = 'books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
    def __repr__(self):
        return "<Book object: {} {}>".format(self.title, self.author)

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    reviewer = models.ForeignKey(User, related_name = 'reviews')
    book = models.ForeignKey(Book, related_name = 'reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
    def __repr__(self):
        return "<Review object: {} {} {}>".format(self.content, self.reviewer, self.book)