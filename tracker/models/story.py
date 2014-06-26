from django.db import models
from project import Project


class Story(models.Model):
    project = models.ForeignKey(Project, related_name='stories')
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    STATE_CHOICES = (
        (0, 'Not Started'),
        (1, 'Started'),
        (2, 'Blocked'),
        (3, 'Finished'),
    )
    state = models.IntegerField(choices=STATE_CHOICES, default=0)
    DIFFICULTY_CHOICES = (
        (0, 'Trivial'),
        (1, 'Easy'),
        (2, 'Difficult'),
        (3, 'Very difficult'),
    )
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=0)
    description = models.TextField()
    assigned_to = models.ForeignKey('auth.User', related_name='stories')

    def _status(self):
        """Returns the story's status."""
        import datetime

        if self.due_date > datetime.date.today():
            return True
        else:
            return False

    _status.boolean = True
    _status.admin_order_field = 'due_date'
    status = property(_status)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        pass

    class Meta:
        ordering = ["due_date"]
        verbose_name_plural = "stories"
        app_label = "tracker"
        permissions = (
            ('view_story', 'Can view stories'),
            ('all_story', 'All permissions story'),
        )

