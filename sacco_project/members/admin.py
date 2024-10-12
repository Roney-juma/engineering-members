from django.contrib import admin

from .models import Member, Project


admin.site.site_header = "Mesk Admin"
admin.site.site_title = "Mesk Admin Portal"
admin.site.index_title = "Welcome to Mesk Admin Portal"

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
