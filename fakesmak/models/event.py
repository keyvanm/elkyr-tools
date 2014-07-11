from django.db import models

from taggit.managers import TaggableManager


class Event(models.Model):
    name = models.CharField(max_length=200)
    host = models.ForeignKey('auth.User', related_name='hosted_events')
    created_at = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    location_lat = models.DecimalField(decimal_places=6, max_digits=9)
    location_long = models.DecimalField(decimal_places=6, max_digits=9)
    address = models.TextField()
    description = models.TextField()
    tags = TaggableManager()  # TODO: look for alternatives
    attendees = models.ManyToManyField('auth.User', related_name='attended_events', blank=True)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.name

    def is_user_an_attendee(self, user):
        return self.attendees.filter(username=user.username).exists()

    class Meta:
        app_label = "fakesmak"
