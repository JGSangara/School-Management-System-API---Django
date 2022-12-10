from django.contrib import admin
from .models import Certificate

# Register your models here.
@admin.register(Certificate)
class Certificate(admin.ModelAdmin):
    list_display = ["name", "description", "created_at", "updated_at"]
    list_filter = ["name", "description", "created_at", "updated_at"]
    search_fields = ["name", "description", "created_at", "updated_at"]