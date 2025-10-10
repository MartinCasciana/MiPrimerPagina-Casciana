from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_kiosco.urls')),
    path('pages/', include('pages.urls')),          # listado/detalle/CRUD
    path('accounts/', include('accounts.urls')),    # login/signup/profile
    path('inbox/', include('inbox.urls')),
    path('about/', include('pages.urls_about')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

