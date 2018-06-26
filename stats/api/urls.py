from django.urls import path

from stats.api import views

urlpatterns = [
    path('changelogs/', views.changelogCLS.as_view(), name='changelog-cls'),
]
