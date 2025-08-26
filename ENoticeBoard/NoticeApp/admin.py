from django.contrib import admin
from .models import Blog
from .models import Notice

# Customize the admin site
admin.site.site_header = "E NOTICE BOARD"
admin.site.index_title = "E NOTICE BOARD"
admin.site.site_title = "E NOTICE BOARD"

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'priority', 'approved', 'created_at')
    list_filter = ('approved', 'category', 'priority')
    search_fields = ('title', 'description', 'tags')
    list_editable = ("approved",)

# Register your models here
admin.site.register(Blog)
