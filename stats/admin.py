from django.contrib import admin

from stats.models import Changelog


class changelog_admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date')


admin.site.register(Changelog, changelog_admin)