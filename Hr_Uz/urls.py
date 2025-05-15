from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from Hr_Uz import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mobileapp/', include('mobileapp.urls', namespace='mobileapp')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
