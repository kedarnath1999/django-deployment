from django.db import models
from django.contrib.auth.models import User
# Create your models here.

## we are adding additional fields to django default user fields
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User) ## we are connecting one to one with the 'user' we are creating and the django default 'User'


    #additional fields
    portfolio_site = models.URLField(blank=True)## can be blank

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)  ## will search in media folder

    def __str__(self):
        return self.user.username   ## will get username from default 'User' cos  user = models.OneToOneField(User)
