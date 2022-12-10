from django.contrib import admin
from .models import WaitList
# Register your models here.


@admin.register(WaitList)
class WaitListAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "is_student", "created_at", "updated_at"]
    list_filter = ["first_name", "last_name", "email", "is_student", "created_at", "updated_at"]
    search_fields = ["first_name", "last_name", "email", "is_student", "created_at", "updated_at"]
