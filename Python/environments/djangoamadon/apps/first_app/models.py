from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    def __repr__(self):
        return "<Product object: {} {}>".format(self.name, self.price) 

class Order(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, related_name = 'product_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Order object: {} {} {}>".format(self.name, self.quantity, self.price) 