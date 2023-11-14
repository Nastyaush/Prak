from django.urls import include

from django.urls import path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]