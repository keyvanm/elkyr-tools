from django.contrib import admin
from django.db.models import Q
from fake_api_gen.models import FakeApi


class FakeApiAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'date_modified', 'slug_link')

    def slug_link(self, obj):
        return u'<a target="__blank" href="/fake_api_gen/fakeapi/%s/">%s</a>' % (obj.slug, obj.slug)
    slug_link.allow_tags = True
    slug_link.short_description = "URL"

    def queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super(FakeApiAdmin, self).queryset(request)
        if request.user.is_superuser:
            # It is mine, all mine. Just return everything.
            return qs
        # Now we just add an extra filter on the queryset and
        # we're done. Assumption: Page.owner is a foreignkey
        # to a User.
        return qs.filter(Q(owner=request.user) | Q(owner__isnull=True))

    # Uncomment to make the object automatically attach to the user who made it
    # def save_model(self, request, obj, form, change):
    #     if not change and not form.cleaned_data["owner"]:
    #         obj.owner = request.user
    #     obj.save()


admin.site.register(FakeApi, FakeApiAdmin)