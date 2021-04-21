from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cron/', include('cron.urls')),
    path('admin/', admin.site.urls),
]
