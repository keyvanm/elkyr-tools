from django.contrib import admin
from django import forms
from django.db import models
from easy_select2 import select2_modelform
from django.db.models import Q

from tracker.models import Story, Project


StoryForm = select2_modelform(Story)
ProjectForm = select2_modelform(Project)


class StoryAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class': 'ckeditor'})}, }
    list_display = ('name', 'project', 'due_date', 'state', 'difficulty', 'assigned_to', '_status', 'description_link',)
    form = StoryForm
    list_filter = ('project', 'due_date', 'state', 'assigned_to',)

    def description_link(self, obj):
        return u'<a target="__blank" href="/api/tracker/stories/%d/description/">Description</a>' % obj.pk

    description_link.allow_tags = True
    description_link.short_description = "URL to description"

    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super(StoryAdmin, self).queryset(request)
        if request.user.is_superuser or request.user.has_perm('tracker.all_story'):
            return qs
        return qs.filter(Q(assigned_to=request.user) | Q(project__contributers=request.user)).distinct()

    class Media:
        js = ("//cdn.ckeditor.com/4.4.2/full/ckeditor.js", '/static/admin/js/story.js',)
        css = {'all': ('/static/admin/css/story.css',)}


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager', 'release_date',)
    form = ProjectForm

    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super(ProjectAdmin, self).queryset(request)
        if request.user.is_superuser or request.user.has_perm('tracker.all_project'):
            return qs
        return qs.filter(Q(manager=request.user) | Q(contributers=request.user)).distinct()


# Register your models here.
admin.site.register(Story, StoryAdmin)
admin.site.register(Project, ProjectAdmin)
