from django.urls import path

from playlist.api import views

urlpatterns = [
    path('', views.playlistCLS.as_view(), name='playlist-cls'),
    path('<int:pk>/', views.playlistRUD.as_view(), name='playlist-rud'),
] 