from django.contrib import admin
from django.urls import path

from app.api import api
from app import views


urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/", api.urls),

    path(
        "api-playground/",
        views.api_playground,
        name="api_playground"
    ),
]