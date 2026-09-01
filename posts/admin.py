from django.contrib import admin
from .models import Post
from django.utils.html import format_html


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "user", "created_at", "updated_at", "image_path")
    search_fields = ("title", "user")
    list_filter = ("title", "user")
    ordering = ("created_at", )


    @admin.display(description="Images")
    def image_path(self, obj):
        if obj.picture:
            return format_html(
                '<img src={} width="40px" height="40px">',
                obj.picture.url
            )
        return "No Images"
