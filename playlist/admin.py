from django.contrib import admin

from playlist.models import Song


class playlist_admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date')


admin.site.register(Song, playlist_admin)