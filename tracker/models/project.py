from django.db import models

class Project(models.Model):
	name = models.CharField(max_length=200)

	manager = models.ForeignKey('auth.User', related_name='managed_projects')

	release_date = models.DateField()

	contributers = models.ManyToManyField('auth.User', related_name='contributed_projects')

	class Meta:
		app_label = "tracker"