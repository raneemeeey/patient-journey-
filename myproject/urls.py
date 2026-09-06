
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # All application URLs
    path("", include("myapp.urls")),
]


