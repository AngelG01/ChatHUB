from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ChatHUB.users.forms import CustomUserCreationForm, CustomUserChangeForm
from ChatHUB.users.models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'password', 'profile_picture', 'bio', 'date_of_birth')


admin.site.register(CustomUser, CustomUserAdmin)
