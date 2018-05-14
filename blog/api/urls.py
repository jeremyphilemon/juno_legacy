from django.urls import path

from blog.api import views

urlpatterns = [
    path('', views.storyCLS.as_view(), name='story-cls'),
    path('<int:pk>/', views.storyRUD.as_view(), name='story-rud'),
]
