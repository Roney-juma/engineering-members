from django.contrib import admin

from .models import Member, EventImage,Event,Blog


admin.site.site_header = "Mesk Admin"
admin.site.site_title = "Mesk Admin Portal"
admin.site.index_title = "Welcome to Mesk Admin Portal"

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'username', 'phone_number', 'membership_number', 'join_date')
    search_fields = ('full_name', 'email', 'username', 'phone_number', 'membership_number')
    list_filter = ('join_date',)
    readonly_fields = ('join_date',)

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1  # Number of empty image fields to display by default for new entries

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'created_at')
    search_fields = ('name', 'description')
    inlines = [EventImageInline]

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author')

# Register your models here
admin.site.register(Event, EventAdmin)
admin.site.register(EventImage)