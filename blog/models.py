from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    """each post can have different categories"""
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} {self.description}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    """ each post can have only one Users """
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.description}'


