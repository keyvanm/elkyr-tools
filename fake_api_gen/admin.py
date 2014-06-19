from django.contrib import admin
from fake_api_gen.models import FakeApi

class FakeApiAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'date_modified', 'slug_link')

    def slug_link(self, obj):
        return u'<a target="__blank" href="/fake_api_gen/fakeapi/%s/">%s</a>' % (obj.slug, obj.slug)
    slug_link.allow_tags = True
    slug_link.short_description = "URL"

    # Uncomment to make the object automatically attach to the user who made it
    # def save_model(self, request, obj, form, change):
    #     if not change and not form.cleaned_data["owner"]:
    #         obj.owner = request.user
    #     obj.save()


admin.site.register(FakeApi, FakeApiAdmin)