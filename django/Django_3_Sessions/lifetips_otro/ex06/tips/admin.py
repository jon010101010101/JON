from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Tu modelo de usuario personalizado

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'reputation', 'is_active', 'is_staff', 'is_superuser')
    ordering = ('username',)