from distutils.command.upload import upload
from email.policy import default
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL

     


class FollowerRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField( blank=True, null=True,upload_to='images/')
    cover = models.ImageField(blank=True, null=True,upload_to='images/')
    location = models.CharField(max_length=220, null=True, blank=True)
    First_Name = models.TextField(blank=True, null=True)
    Last_Name = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    premium = models.BooleanField('default'=False)
    age = models.TextField(blank=True, null=True)
    height = models.TextField(blank=True, null=True)
    weight = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    """
    project_obj = Profile.objects.first()
    project_obj.followers.all() -> All users following this profile
    user.following.all() -> All user profiles I follow
    """
    def user_did_save(sender, instance, created, *args, **kwargs):
        if created:
            Profile.objects.get_or_create(user=instance)

    post_save.connect(user_did_save, sender=User)

class Training(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField( blank=True, null=True,upload_to='images/')
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    location = models.CharField(max_length=220, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    age = models.TextField(blank=True, null=True)
    height = models.TextField(blank=True, null=True)


class Academics(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField( blank=True, null=True,upload_to='images/')
    cover = models.ImageField(blank=True, null=True,upload_to='images/')
    location = models.CharField(max_length=220, null=True, blank=True)
    First_Name = models.TextField(blank=True, null=True)
    Last_Name = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    age = models.TextField(blank=True, null=True)
    height = models.TextField(blank=True, null=True)
