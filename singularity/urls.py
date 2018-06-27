from django.contrib import admin
from django.urls import include, path

from singularity import views

from rest_framework.authtoken import views as authView

urlpatterns = [
    path('', views.singularity, name='singularity'),
    path('api/', include('rest_framework.urls')),
    path('api/stories/', include('blog.api.urls')),
    path('api/stats/', include('stats.api.urls')),
    path('api/playlist/', include('playlist.api.urls')),
    path('api/auth-token/', authView.obtain_auth_token),
    path('admin/', admin.site.urls),
]
