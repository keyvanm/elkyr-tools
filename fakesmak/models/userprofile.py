from django.db import models
from taggit.managers import TaggableManager


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', related_name="profile")
    profile_picture = models.ImageField(upload_to="profile_pics")
    bio = models.TextField()
    is_verified_facebook = models.BooleanField(default=False)
    is_verified_text = models.BooleanField(default=False)
    date_of_birth = models.DateField()
    interests = TaggableManager()
