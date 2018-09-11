from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Course object: {} {} {}>".format(self.name, self.desc) 