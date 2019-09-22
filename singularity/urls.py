from django.contrib import admin
from django.urls import include, path

from singularity import views

from rest_framework.authtoken import views as authView

urlpatterns = [
    path('', views.singularity, name='singularity'),
    path('fluff/<int:id>/', views.story, name='story'),
    path('fluff/', views.fluff, name='fluff'),
    path('api/', include('rest_framework.urls')),
    path('api/stories/', include('blog.api.urls')),
    path('api/stats/', include('stats.api.urls')),
    path('api/auth-token/', authView.obtain_auth_token),
    path('admin/', admin.site.urls),
    path('jet_api/', include('jet_django.urls')),
]
