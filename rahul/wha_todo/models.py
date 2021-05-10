from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class work(models.Model):
    todo = models.CharField(max_length=20)
    def __str__(self):
	       return self.todo

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio = models.URLField(blank= True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank = True)
    def __str__(self):
        return self.user.username
