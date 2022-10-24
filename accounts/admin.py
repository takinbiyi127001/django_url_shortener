from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .forms import CustonUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustonUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "is_superuser"]


admin.site.register(CustomUser, CustomUserAdmin)