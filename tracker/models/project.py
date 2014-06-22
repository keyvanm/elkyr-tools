from django.db import models

class Project(models.Model):
	name = models.CharField(max_length=200)

	manager = models.ForeignKey('auth.User', related_name='managed_projects')

	created_at = models.DateTimeField(auto_now_add=True)
	release_date = models.DateField()

	contributers = models.ManyToManyField('auth.User', related_name='contributed_projects')

	def __unicode__(self):
		return self.name

	class Meta:
		app_label = "tracker"
		permissions = (
			('all_project', 'All permissions project'),
		)