from django.contrib import admin
from .models import Lecture
# Register your models here.

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at', 'updated_at', 'slides_url']
    list_filter = ['title', 'description', 'created_at', 'updated_at', 'slides_url']
    search_fields = ['title', 'description', 'created_at', 'updated_at', 'slides_url']


