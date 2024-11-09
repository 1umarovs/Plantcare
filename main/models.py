from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Plants(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')
    body = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    old_price = models.FloatField()
    new_price = models.FloatField()

    def __str__(self) -> str:
        return self.title

class Addition(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')
    old_price = models.FloatField()
    new_price = models.FloatField()

    def __str__(self) -> str:
        return self.title

class Addblog(models.Model):
    image = models.ImageField(upload_to='images/')
    author = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


