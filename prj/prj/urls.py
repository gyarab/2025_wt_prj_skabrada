
from django.contrib import admin
from django.urls import path


from app.api import api


urlpatterns = [
    path("api/", api.urls),
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
