from django.contrib import admin
from .models import Work

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'created']
    list_filter = ['status', 'created']
    search_fields = ['title', 'description']