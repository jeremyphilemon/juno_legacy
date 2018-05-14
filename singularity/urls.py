from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('fluff/', include('blog.urls'), name='blog'),
    path('api/', include('rest_framework.urls')),
    path('api/stories/', include('blog.api.urls')),
    path('admin/', admin.site.urls),
]
