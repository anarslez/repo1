from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Book object: {} {}>".format(self.name, self.desc)
class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Author object: {} {} {}>".format(self.first_name, self.last_name, self.email)
class Book_Author(models.Model):
    books = models.ForeignKey(Book)
    authors = models.ForeignKey(Author)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Book_Author object: {} {}>".format(self.books, self.authors)