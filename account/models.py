from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    User = models.OneToOneField(User)
    description = models.CharField(max_length=100,default=' ')
    city = models.CharField(max_length=100,default=' ')
    website = models.URLField(default =' ')
    mobile_no = models.IntegerField(default = 0)
    image  = models.ImageField(blank = True ,upload_to = 'profile_image')

    def __str__(self):
        return self.User.username
def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(User = kwargs['instance'])
post_save.connect(create_profile,sender = User)