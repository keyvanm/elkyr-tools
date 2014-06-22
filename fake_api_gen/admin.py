from django.contrib import admin
from django.db.models import Q
from fake_api_gen.models import FakeApi
from guardian.admin import GuardedModelAdmin


class FakeApiAdmin(GuardedModelAdmin):
    list_display = ('name', 'owner', 'date_modified', 'slug_link')
    prepopulated_fields = {"slug": ("name",)}

    def slug_link(self, obj):
        return u'<a target="__blank" href="%s">%s</a>' % (obj.get_absolute_url(), obj.slug)
    slug_link.allow_tags = True
    slug_link.short_description = "URL"

    def get_queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super(FakeApiAdmin, self).queryset(request)
        if request.user.is_superuser:
            # It is mine, all mine. Just return everything.
            return qs
        # Now we just add an extra filter on the queryset and
        # we're done.
        return qs.filter(Q(owner=request.user) | Q(owner__isnull=True))

    # Uncomment to make the object automatically attach to the user who made it
    # def save_model(self, request, obj, form, change):
    #     if not change and not form.cleaned_data["owner"]:
    #         obj.owner = request.user
    #     obj.save()


admin.site.register(FakeApi, FakeApiAdmin)