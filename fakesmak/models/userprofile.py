import datetime

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', related_name="profile")
    avatar = models.ImageField(upload_to="avatars")
    bio = models.TextField()
    is_verified_facebook = models.BooleanField(default=False)
    is_verified_text = models.BooleanField(default=False)
    date_of_birth = models.DateField()
    interests = TaggableManager()

    def __unicode__(self):
        return "%s's profile" % self.user.username


# automatically make a user profile when a user is created
def create_user_profile(sender, **kwargs):
    """When creating a new user, make a profile for him or her."""
    created = kwargs["created"]
    if created:
        u = kwargs["instance"]
        if not UserProfile.objects.filter(user=u):
            user_profile = UserProfile(user=u, date_of_birth=datetime.date.today(), bio="Write your bio here")
            user_profile.save()


post_save.connect(create_user_profile, sender=User)