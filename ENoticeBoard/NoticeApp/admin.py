from django.contrib import admin
from .models import Blog

# Customize the admin site
admin.site.site_header = "E NOTICE BOARD"
admin.site.index_title = "E NOTICE BOARD"
admin.site.site_title = "E NOTICE BOARD"

# Register your models here
admin.site.register(Blog)
