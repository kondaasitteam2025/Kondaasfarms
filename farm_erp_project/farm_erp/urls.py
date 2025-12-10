from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dashboard import views as dashboard_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_views.home, name='home'),
    path('core/', include('core.urls')),
    path('farm/', include('farm.urls')),
    path('fertigation/', include('fertigation.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
