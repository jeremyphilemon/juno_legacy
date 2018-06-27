from django.urls import path

from playlist.api import views

urlpatterns = [
    path('', views.playlistCLS.as_view(), name='playlist-cls'),
] 