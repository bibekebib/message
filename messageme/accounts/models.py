from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=False)
    photo = models.ImageField(default='default.jpeg', upload_to='userimage/')
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username}'s profile"
