from django.urls import path

from playlist.api import views

urlpatterns = [
    path('', views.playlistCLS.as_view(), name='playlist-cls'),
    path('<int:pk>/', views.playlistRUD.as_view(), name='playlist-rud'),
    path('<int:pk>/heart/', views.songHeart.as_view(), name='song-heart-rud'),
    path('<int:pk>/view/', views.songView.as_view(), name='song-view-rud'),
] 