from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "is_staff", "is_superuser", "created_at", "updated_at")
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("bio", "profile_picture")}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("bio", "profile_picture")}),
    )
