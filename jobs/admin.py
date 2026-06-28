from django.contrib import admin
from .models import Company, Job


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'location', 'created_at']
    search_fields = ['name', 'location']


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'job_type', 'experience_level', 'is_active', 'created_at']
    list_filter = ['job_type', 'experience_level', 'is_active']
    search_fields = ['title', 'company__name']