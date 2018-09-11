from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Dojo object: {} {} {}>".format(self.name, self.city, self.state)
class Ninja(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    classroom = models.ForeignKey(Dojo)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Ninja object: {} {} {}>".format(self.first_name, self.last_name, self.classroom)