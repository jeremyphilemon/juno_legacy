from django.contrib import admin
from django.urls import include, path

from singularity import views

urlpatterns = [
    path('', views.singularity, name='singularity'),
    path('api/', include('rest_framework.urls')),
    path('api/stories/', include('blog.api.urls')),
    path('api/stats/', include('stats.api.urls')),
    path('admin/', admin.site.urls),
]
