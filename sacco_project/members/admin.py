from django.contrib import admin

from .models import Member, Project
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'username', 'phone_number', 'membership_number', 'join_date')
    search_fields = ('full_name', 'email', 'username', 'phone_number', 'membership_number')
    list_filter = ('join_date',)
    readonly_fields = ('join_date',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('start_date', 'end_date')
    readonly_fields = ('created_at', 'updated_at')
