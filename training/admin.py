from django.contrib import admin
from  .models import *
# Register your models here.
class ErrorTypeAdmin(admin.ModelAdmin):
    list_display = (
        'error_title', 'max_value', 'avg_value', 'created_at'
    )
    list_display_links = ('error_title', 'max_value', 'avg_value',)
    list_filter = ["created_at"]
    search_fields = ('error_title', 'created_at')

admin.site.register(ERRORTYPE, ErrorTypeAdmin)