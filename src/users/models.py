from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    username= models.OneToOneField(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=120)

    def __str__(self):
        return f"Profile of {self.username.username}"
