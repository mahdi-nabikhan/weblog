from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    """each post can have different categories"""
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.name} {self.description}'


class Post(models.Model):
    """author can have different posts with different categories """
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ['-updated_at','-created_at']

    def __str__(self):
        return f'{self.title} {self.description}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'post_id': self.id})
