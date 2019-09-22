from django.contrib import admin

from blog.models import Story


class story_admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'archived')


admin.site.register(Story, story_admin)
