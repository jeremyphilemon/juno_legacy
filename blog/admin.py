from django.contrib import admin

from blog.models import Story


class story_admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'story', 'date')


admin.site.register(Story, story_admin)
