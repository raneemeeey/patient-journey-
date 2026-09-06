
from django.contrib import admin
from .models import Surgery


@admin.register(Surgery)
class SurgeryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "specialty",
        "subspecialty",
        "created_at",
    )

    list_filter = (
        "specialty",
        "subspecialty",
    )

    search_fields = (
        "name",
        "short_description",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }
