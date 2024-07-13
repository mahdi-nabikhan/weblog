from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    age = models.PositiveIntegerField()
    email = models.EmailField()
    phone_number = models.PositiveIntegerField(max_length=11)

    def __str__(self):
        return f'{self.user.username} {self.bio}'
